from django.shortcuts import render, redirect
import markdown
# Create your views here.
# 导入HttpResponse模块
from django.http import HttpResponse
# 导入数据模型ArticlePost
from article.models import ArticlePost, ArticleColumn
# 引入刚才定义的ArticlePostForm表单类
from article.forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# 引入分页
from django.core.paginator import Paginator 
# 引入Q对象
from django.db.models import Q
from comment.models import Comment

# 视图函数
def article_list(request):
    # 从url中提取查询参数
    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')

    # 初始化查询集
    article_list = ArticlePost.objects.all()
    
    # 用户搜索逻辑
    if search:
        article_list = article_list.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        # 将search参数重置为空
        search = ''

    # 栏目查询集
    if column is not None and column.isdigit():
        article_list = article_list.filter(column=column)
    
    # 标签查询集
    if tag and tag != 'None':
        article_list = article_list.filter(tags__name__in=[tag])
    
    # 查询集排序
    if order == 'total_views':
        article_list = article_list.order_by('-total_views')

    # 每页显示 2 篇文章
    paginator = Paginator(article_list, 2)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)

    context = { 
        'articles': articles,
        'order': order,
        'search': search,
        'column': column,
        'tag': tag,
    }
    return render(request, 'article/list.html', context)

# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    # 取出文章评论
    comments = Comment.objects.filter(article=id)
    # 浏览量加一
    article.total_views += 1
    article.save(update_fields=['total_views'])
    # 将markdown语法渲染成html格式
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
        ]
    )
    article.body = md.convert(article.body)
    # 选哟传递给模板的对象
    context = {
        'article': article,
        'toc': md.toc,
        'comments': comments
    }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)

# 写文章的视图
@login_required(login_url='/userprofile/login/')
def article_create(request):
    # 判断用户是否提交数据
    if request.method == 'POST':
        # 将提交的数赋值到表单实例中
        article_post_form = ArticlePostForm(request.POST, request.FILES)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中id=1的用户为作者
            # 如果你进行过删除数据库的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=request.user.id)
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])
            # 将新文章保存到数据库中
            new_article.save()
            #? 新增代码，保存tags的多对多关系
            article_post_form.save_m2m()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        # 赋值上下文
        context = {
            'article_post_form': article_post_form,
            'columns': columns
        }
        # 返回模板
        return render(request, 'article/create.html', context)

# 删除文章
def article_delete(request, id):
    """
    先根据id获取需要删除的文章
    然后，调用.delete()方法删除文章
    完成删除后，返回文章列表
    """
    if request.user != article.user:
        return HttpResponse("抱歉，你无权删除这篇文章。")
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")

# 安全删除文章
@login_required(login_url='/userprofile/login/')
def article_safe_delete(request, id):
    """
    判断是不是post请求
    如果是post请求,先根据id获取需要删除的文章
    然后，调用.delete()方法删除文章
    完成删除后，返回文章列表
    如果不是,则返回仅允许post请求
    """
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        if request.user != article.author:
            return HttpResponse("抱歉，你无权修改这篇文章。")
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")

# 更新文章
def article_update(request, id):
    """
    更新文章的视图函数
    通过post方法提交表单,更新title、body字段
    get方法进入初始表单页面
    id: 文章的id
    """
    """
    获取需要修改的具体文章对象
    判断用户是否为post提交表单数据
        将提交的数据赋值到表单实例中
        判断提交的数据是否满足模型的要求
            保存新写入的title、body数据并保存
            完成后返回到修改后的文章中。需要传入文章的id值
        如果数据不合法，返回错误信息
    如果用户get请求获取数据
        创建表单类实例
        赋值上下文,将article文章对象也传递进去,以便提取旧的内容
        将响应返回到模板中
    """
    article = ArticlePost.objects.get(id=id)
    # 过滤非作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")
    
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.body = request.POST['body']
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        context = {
            'article': article,
            'article_post_form': article_post_form,
            'columns': columns
        }
        return render(request, 'article/update.html', context)
