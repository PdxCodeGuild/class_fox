from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("fox/", views.fox),
    path("osprey/", views.osprey),
    path("<str:class_name>/", views.cohort),
]
