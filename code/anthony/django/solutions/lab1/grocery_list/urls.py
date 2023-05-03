from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    path('toggle_purchased/<int:item_id>/',
         views.toggle_purchased, name='toggle_purchased'),
    path('delete/<int:item_id>/',
         views.delete_item, name='delete_item'),
]

# root     / project.urls / app.urls
# 127.0.0.1/                        -> home
# 127.0.0.1/ add_item     /         -> add_item
# 127.0.0.1/ toggle_purchased / 3   -> toggle_purchased
