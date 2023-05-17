from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:link>/', views.delete_item, name='delete_item'),
    path('r/<code>', views.redirect_link, name='redirect_link'),
    path('add_link', views.add_link, name='add_link'),
    path('', views.home, name='home'),
]