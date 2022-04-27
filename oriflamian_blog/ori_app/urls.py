from django.urls import path

from oriflamian_blog.ori_app.views.generic import HomeView, DashboardView

from oriflamian_blog.ori_app.views.posts import PostDetailsView, CreatePostView, EditPostView, DeletePostView

from oriflamian_blog.ori_app.views.reviews import ReviewDetailsView, CreateReviewView, EditReviewView, DeleteReviewView
from oriflamian_blog.ori_app.views.store import store, product_details

urlpatterns = (

    path('', HomeView.as_view(), name='home page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('post/details/<int:pk>/', PostDetailsView.as_view(), name='post details'),
    path('post/add/', CreatePostView.as_view(), name='create post'),
    path('post/edit/<int:pk>/', EditPostView.as_view(), name='edit post'),
    path('post/delete/<int:pk>/', DeletePostView.as_view(), name='delete post'),

    path('review/details/<int:pk>/', ReviewDetailsView.as_view(), name='review details'),
    path('review/create/', CreateReviewView.as_view(), name='create review'),
    path('review/edit/<int:pk>/', EditReviewView.as_view(), name='edit review'),
    path('review/delete/<int:pk>/', DeleteReviewView.as_view(), name='delete review'),

    path('store/', store, name='store'),
    path('product/<int:pk>/', product_details, name='product details'),


)
