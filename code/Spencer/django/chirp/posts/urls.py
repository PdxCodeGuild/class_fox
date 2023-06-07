from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('post/create/', views.post_create, name='post-create'),
]

