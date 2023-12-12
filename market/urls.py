from . import views
from django.urls import path
from .views import PostCreate


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post-detail/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post-form/', PostCreate.as_view(), name='post_form'),
]