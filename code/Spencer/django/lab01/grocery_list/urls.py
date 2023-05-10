from django.urls import path
from . import views

urlpatterns = [
    path('add_items/', views.add_item, name='add_item'),
    path('', views.home, name='home'),
    path('mark_purchased/<int:item_id>/', views.mark_purchased, name='mark_purchased'),
    path('not_purchased/<int:item_id>/', views.mark_purchased, name='not_purchased'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]