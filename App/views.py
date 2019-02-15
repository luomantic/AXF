from django.shortcuts import render
from .models import *


# Create your views here.


# 首页
def home(request):
    # 轮播数据
    wheels = MainWheel.objects.all()
    # 导航数据
    navs = MainNav.objects.all()
    # 必购数据
    mustbuys = MainMustBuy.objects.all()
    # shop数据
    shops = MainShop.objects.all()
    shop0 = shops.first()
    shops_12 = shops[1:3]
    shops_36 = shops[3:7]
    shops_710 = shops[7:11]

    data = {
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shop0': shop0,
        'shops_12': shops_12,
        'shops_36': shops_36,
        'shops_710': shops_710,
    }

    return render(request, 'home/home.html', data)


# 闪购
def market(request):
    return render(request, 'market/market.html')


# 购物车
def cart(request):
    return render(request, 'cart/cart.html')


# 我的
def mine(request):
    return render(request, 'mine/mine.html')
