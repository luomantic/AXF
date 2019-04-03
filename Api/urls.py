from django.urls import path,re_path
from . import views


app_name = 'Api'

urlpatterns = [
    path('author/', views.author, name='author'),
]
