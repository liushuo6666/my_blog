from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import ArticlePost
from comment.forms import CommentForm
from comment.models import Comment
from notifications.signals import notify
from django.contrib.auth.models import User
# Create your views here.

# 文章评论
@login_required(login_url='/userprofile/login/')
#? 新增参数parent_comment_id
def post_comment(request, article_id, parent_comment_id=None):
    article = get_object_or_404(ArticlePost, id=article_id)

    # 处理POST请求
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user

            #? 二级回复
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                #? 若回复层级超过二级，则转换为二级
                new_comment.parent_id = parent_comment.get_root().id
                new_comment.save()
                #! 给其他用户发送通知
                if not parent_comment.user.is_superuser:
                    notify.send(
                        request.user,
                        recipient=parent_comment.user,
                        verb='回复了你',
                        target=article,
                        action_object=new_comment,
                    )
                return HttpResponse("200, ok")
            
            new_comment.save()
            #! 给管理员发送通知
            if not request.user.is_superuser:
                notify.send(
                        request.user,
                        recipient=User.objects.filter(is_superuser=1),
                        verb='回复了你',
                        target=article,
                        action_object=new_comment,
                    )
            return redirect(article)
        else:
            return HttpResponse("表单内容有误，请重新填写")
    #? 处理get请求
    elif request.method == "GET":
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'article_id': article_id,
            'parent_comment_id': parent_comment_id,
        }
        return render(request, 'comment/reply.html', context)
    else:
        return HttpResponse("发表评论仅接受POST请求")    
    