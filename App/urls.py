from django.urls import path, include, re_path
from . import views

app_name = 'App'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    re_path('marketwithparams/(\d+)/(\d+)/(\d+)/$', views.market_with_params, name='market_with_params'),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),
    path('register/', views.register, name='register'),
    path('register_handle/', views.register_handle, name='register_handle'),
]
