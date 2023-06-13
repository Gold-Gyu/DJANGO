from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path("index/" , views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("fruits/", views.fruits, name="fruits"),
    path("template/", views.template, name="template"),
]
