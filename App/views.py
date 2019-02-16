from django.shortcuts import render, redirect, reverse
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
    # 主要商品数据
    mainshows = MainShow.objects.all()

    data = {
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shop0': shop0,
        'shops_12': shops_12,
        'shops_36': shops_36,
        'shops_710': shops_710,
        'mainshows': mainshows,
    }

    return render(request, 'home/home.html', data)


# 闪购
def market(request):
    return redirect(reverse('App:market_with_params', args=[104749]))


# 闪购 - 带参数
def market_with_params(request, typeid):
    # 左面的的导航///
    foodtypes = FoodType.objects.all()
    # 商品数据, 根据主分类id进行筛选
    goods_list = Goods.objects.filter(categoryid=typeid)
    # 获取当前主分类下的所有子分类
    foodset = FoodType.objects.filter(typeid=typeid)

    child_type_list = []  # 存放子分类的数据
    if foodset.exists():
        childtypes = foodset.first().childtypenames.split('#')
        # childtypes ['全部分类:0', '进口水果:103534', '国产水果:103533']
        for childtype in childtypes:
            type_list = childtype.split(':')
            child_type_list.append(type_list)
            # child_type_list [['全部分类', '0'], ['进口水果', '103534'], ['国产水果', '103533']]

    data = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'typeid': typeid,
        'child_type_list': child_type_list,
    }
    return render(request, 'market/market.html', data)


# 购物车
def cart(request):
    return render(request, 'cart/cart.html')


# 我的
def mine(request):
    return render(request, 'mine/mine.html')
