from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/create/', views.create_post, name='create-post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit-post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete-post'),
]
