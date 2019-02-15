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


# 主要商品
class MainShow(Main):
    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=20)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=20)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_mainshow'

# trackid,name,img,
# categoryid,brandname,
# img1,childcid1,productid1,longname1,price1,marketprice1,
# img2,childcid2,productid2,longname2,price2,marketprice2,
# img3,childcid3,productid3,longname3,price3,marketprice3
