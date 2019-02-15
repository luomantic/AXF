from django.db import models


# Create your models here.

# 首页
class Main(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True  # 抽象类，不会被生成表


# 首页 - 轮播
class MainWheel(Main):
    class Meta:
        db_table = 'axf_wheel'


# 首页 - 导航
class MainNav(Main):
    class Meta:
        db_table = 'axf_nav'


# 首页 - 必购
class MainMustBuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


# 首页 - shop
class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'
