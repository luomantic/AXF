from django.shortcuts import render, redirect, reverse
from .models import *
import hashlib


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
    return redirect(reverse('App:market_with_params', args=[104749, '0', '0']))


# 闪购 - 带参数
def market_with_params(request, typeid, typechildid, sortid):
    # 左面的的导航///
    foodtypes = FoodType.objects.all()
    # 商品数据, 根据主分类id进行筛选
    goods_list = Goods.objects.filter(categoryid=typeid)

    # 再按照子分类进行筛选
    if typechildid != '0':
        goods_list = goods_list.filter(childcid=typechildid)

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

    # 排序规则
    if sortid == '0':  # 综合排序
        pass
    elif sortid == '1':  # 销量排序
        goods_list = goods_list.order_by('-productnum')
    elif sortid == '2':  # 价格升序
        goods_list = goods_list.order_by('price')
    elif sortid == '3':  # 价格降序
        goods_list = goods_list.order_by('-price')

    data = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'typeid': typeid,
        'child_type_list': child_type_list,
        'typechildid': typechildid,
    }
    return render(request, 'market/market.html', data)


# 我的
def mine(request):
    return render(request, 'mine/mine.html')


# 注册
def register(request):
    return render(request, 'user/register.html')


# 密码加密
def has_code(s, salt='axf_luomantic'):  # 加盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


# 注册操作
def register_handle(request):
    data = {
        'status': 1,
        'msg': 'ok',
    }

    if request.method == 'POST':
        # 获取post提交的数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        # 对提交的数据，进行后台合法性校验
        if len(username) < 6:
            data['status'] = 0
            data['msg'] = '用户名不合法'
            return render(request, 'user/register.html', data)

        # 检测用户是否重复
        is_username_exist = User.objects.filter(name=username)
        if is_username_exist:
            data['status'] = 0
            data['msg'] = "用户名已存在"
            return render(request, 'user/register.html')

        # 判断两次密码是否一致, 等各种检测

        # 创建用户并保存到数据库
        user = User()
        user.name = username
        user.password = has_code(password)  # 后台存储的时候使用密码加密
        user.email = email
        user.icon = icon
        user.save()

        return redirect(reverse('App:mine'))

    return redirect(reverse('App:register'))


# 购物车
def cart(request):
    return render(request, 'cart/cart.html')
