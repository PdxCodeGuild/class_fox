from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_link/", views.add_link, name="new_link"),
    path("r/<str:url_code>/", views.redirect_link, name="redirect_link"),
    path("delete/<int:link_id>/", views.delete_link, name="delete_link")
]
