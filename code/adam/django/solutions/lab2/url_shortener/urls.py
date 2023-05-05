from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_link', views.add_link, name='add_link'),
    path('r/<str:code>', views.redirect_link, name='redirect_link'),
    path('delete/<int:link_id>/',views.delete_link, name='delete_link'),
]
