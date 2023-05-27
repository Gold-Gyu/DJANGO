from django.urls import path
from . import views
app_name = "myapp2"
urlpatterns = [
    path("hello/<name>/", views.hello, name="hello")
]
