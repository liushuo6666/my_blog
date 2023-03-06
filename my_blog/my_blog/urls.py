"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import notifications.urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 新增代码，配置app的url
    path('article/', include(('article.urls', 'article'),namespace='article')),
    # 用户管理
    path('userprofile/', include(('userprofile.urls', 'userprofile'),namespace='userprofile')),
    path('password_reset/', include('password_reset.urls')),
    # 评论
    path('comment/', include(('comment.urls', 'comment'), namespace='comment')),
    # 消息通知
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # 消息已读未读
    path('notice/', include(('notice.urls', 'notice'),namespace='notice')),
]

# 配置图片的路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
