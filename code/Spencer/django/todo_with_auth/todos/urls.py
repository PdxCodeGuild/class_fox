from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [ 
    path("auth/", include('users.urls')),
    path("", views.home, name="home"),
    path("create-todo/", views.create_todo, name="create_todo")
]