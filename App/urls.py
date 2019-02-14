from django.urls import path, include
from . import views

app_name = 'App'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),
]
