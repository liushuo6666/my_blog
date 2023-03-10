from django.urls import path
from notice import views

urlpatterns = [
    # 通知列表
    path('list/', views.CommentNoticeUpdateView.as_view(), name='list'),
    # 更新通知状态
    path('update/', views.CommentNoticeUpdateView.as_view(), name='update'),
]
