from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    # 상대방으로부터 데이터를 입력받을 화면을 보여줄 new
    path('create/', views.create, name='create'),
    # 사용자가 데이터를 보냈을 때 저장하는 create

    #삭제 요청 처리
    path('<int:pk>/delete/', views.delete, name="delete"),

    # 수정 처리 중 화면만을 위한 경로
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/update/", views.update, name="update"),


]
