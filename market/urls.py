from . import views
from django.urls import path
from .views import PostCreate


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post-detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post-form/', PostCreate.as_view(), name='post_form'),
    path('post/update/<slug:slug>/', views.PostUpdate.as_view(), name='post_update_form'),
    path('post/delete/<slug:slug>/', views.PostDelete.as_view(), name='post_delete'),
    path('comment/update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update_form'),
    path('comment/delete/<int:comment_id>/', views.CommentDelete.as_view(), name='comment_delete'),
]
