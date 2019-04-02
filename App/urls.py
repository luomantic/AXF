from django.urls import path, re_path

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
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('login_handle/', views.login_handle, name='login_handle'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('addnum/', views.add_num, name='add_num'),
    path('reducenum/', views.reduce_num, name='reduce_num'),
    path('delcart/', views.del_cart, name='del_cart'),
    path('cartselect/', views.cart_select, name='cart_select'),
    path('cartselectall/', views.cart_selectall, name='cart_selectall'),
    path('ordercreate/', views.order_create, name='order_create'),
    re_path('order/(\d+)/$', views.order, name='order'),
    path('order_change_status/', views.order_change_status, name='order_change_status'),
    path('order_wait_pay/', views.order_wait_pay, name='order_wait_pay'),
    path('order_paid/', views.order_paid, name='order_paid'),
    path('order_wait_evaluate/', views.order_wait_evaluate, name='order_wait_evaluate'),
]
