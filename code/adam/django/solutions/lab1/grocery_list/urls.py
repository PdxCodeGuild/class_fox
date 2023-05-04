from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    path('mark_purchased/<int:item_id>/', views.mark_purchased, name='mark_purchased'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item')

]
