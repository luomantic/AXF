from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse

from .models import *


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
    data = {
        'name': "",
        "icon": "",
    }

    user_id = request.session.get('user_id', None)

    if user_id:
        user = User.objects.get(id=user_id)
        name = user.name
        icon = user.icon
        data['name'] = name
        data['icon'] = '/upload/icon/' + icon.name
        return render(request, 'mine/mine.html', data)
    return render(request, 'mine/mine.html')


# 注册
def register(request):
    return render(request, 'user/register.html')


# 密码加密 ———— 暂时不做加密存储，注意加密后密码的长度


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
            return render(request, 'user/register.html', data)

        # 判断两次密码是否一致, 等各种检测

        # 创建用户并保存到数据库
        user = User()
        user.name = username
        user.password = password
        user.email = email
        user.icon = icon
        user.save()

        # 保存session
        # request.session['user_id'] = user.id
        # return redirect(reverse('App:login'))

    return redirect(reverse('App:register'))


# 退出登录
def logout(request):
    # request.session.flush()
    del request.session['user_id']  # 删除user_id的session
    return redirect(reverse('App:mine'))


# 登录
def login(request):
    return render(request, 'user/login.html')


def login_handle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 去数据库取用户名密码（忽略解密操作）
        users = User.objects.filter(name=username, password=password)
        if users.exists():
            # 保存session,注意users是一个字典
            request.session['user_id'] = users.first().id
            request.session.set_expiry(0)  # 此处设置关闭浏览器清除session
            # 登录成功，返回我的页面
            return redirect(reverse('App:mine'))
        else:
            # 返回提示消息，用户名或密码错误
            return render(request, 'user/login.html', {'msg': '用户名或密码错误'})
    return render(request, 'user/login.html', {'msg': 'ok'})


# 购物车
def cart(request):
    # 检查是否已登录
    userid = request.session.get('user_id')
    if not userid:
        return redirect(reverse('App:login'))
    else:
        carts = Cart.objects.filter(user_id=userid)
        return render(request, 'cart/cart.html', {'carts': carts})


# 加入购物车
def add_to_cart(request):
    data = {
        'status': 1,
        'msg': 'ok',
    }
    # 判断用户是否登录，如果没有登录，跳转到登录页面
    userid = request.session.get('user_id')
    if not userid:
        data['status'] = 0
        data['msg'] = '用户未登录'
        # return redirect(reverse('App:login'))
    else:
        if request.method == "GET":
            good_id = request.GET.get('goods_id')
            goods_num = request.GET.get('goods_num')

            # 判断该商品是否已经在该用户的购物车中
            carts = Cart.objects.filter(user_id=userid, goods_id=good_id)

            if carts.exists():
                temp_cart = carts.first()
                temp_cart.num += int(goods_num)
                temp_cart.save()
            else:
                # 添加到购物车
                temp_cart = Cart()
                temp_cart.user_id = userid
                temp_cart.goods_id = good_id
                temp_cart.num = goods_num
                temp_cart.save()
        else:
            data['status'] = -1
            data['msg'] = "请求方式不正确"
    return JsonResponse(data)


# 数量+
def add_num(request):
    data = {
        'status': 1,
        'msg': 'ok',
    }

    userid = request.session.get('user_id')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':
            cartid = request.GET.get('cartid')

            temp_goods = Cart.objects.get(id=cartid)
            temp_goods.num += 1
            temp_goods.save()
            data['num'] = temp_goods.num
        else:
            data['status'] = -1
            data['msg'] = '请求方式不正确'
    return JsonResponse(data)


# 数量-
def reduce_num(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    userid = request.session.get('user_id')
    if not userid:
        data['status'] = 0
        data['msg'] = "未登录"
    else:
        if request.method == 'GET':
            cartid = request.GET.get('cartid')

            temp_goods = Cart.objects.get(id=cartid)
            temp_goods.num -= 1
            if temp_goods.num < 1:
                temp_goods.num = 1
            temp_goods.save()
            data['num'] = temp_goods.num
        else:
            data['status'] = -1
            data['msg'] = '请求方式不正确'
    return JsonResponse(data)


# 删除
def del_cart(request):
    data = {
        'status': 1,
        'msg': 'ok',
    }

    userid = request.session.get('user_id')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':
            cartid = request.GET.get('cartid')
            Cart.objects.filter(id=cartid).delete()
        else:
            data['status'] = -1
            data['msg'] = '请求方式不正确'
    return JsonResponse(data)


# 勾选/取消勾选
def cart_select(request):
    data = {
        'status': 1,
        'msg': 'ok',
    }

    userid = request.session.get('user_id')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':
            cartid = request.GET.get('cartid')
            temp_goods = Cart.objects.get(id=cartid)
            temp_goods.is_select = not temp_goods.is_select
            temp_goods.save()

            data['is_select'] = temp_goods.is_select
        else:
            data['status'] = -1
            data['msg'] = '请求方式不正确'
    return JsonResponse(data)
