from django.urls import path
from . import views
urlpatterns = [
    #转移url请求到views
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]