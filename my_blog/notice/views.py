from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from article.models import ArticlePost

# Create your views here.

class CommentNoticeView(LoginRequiredMixin, ListView):
    """
    通知列表
    上下文的名称
    模板位置
    登陆重定向
    """
    context_object_name = 'notice'
    template_name = 'notice/list.html'
    login_url = '/userprofile/login/'
    # 未读通知的查询集
    def get_queryset(self):
        return self.request.user.notification.unread() 

class CommentNoticeUpdateView(View):
    """
    更新通知状态
    处理get请求
        获取未读消息
        更新单条通知
        更新全部通知
    """
    def get(self, request):
        notice_id = request.GET.get('notice_id')
        if notice_id:
            article = ArticlePost.objects.get(id=request.GET.get('article_id'))
            request.user.notifications.get(id=notice_id).mark_as_read()
            return redirect(article)
        else:
            request.user.notifications.mark_all_as_read()
            return redirect('notice:list')
