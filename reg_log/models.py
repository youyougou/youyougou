from django.db import models


class Users(models.Model):
    uid = models.IntegerField()
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    pwd = models.CharField(max_length=100)


class Goods(models.Model):
    logo_img = models.CharField(max_length=150)
    product_name = models.CharField(max_length=200)
    product_img = models.CharField(max_length=150)
    dealer_name = models.CharField(max_length=50)
    product_size = models.CharField(max_length=20)
    product_detail_img = models.CharField(max_length=150)
    category_id = models.FloatField()
    child_id = models.FloatField()
    dealer_id = models.FloatField()
    product_id = models.FloatField()
    price = models.FloatField()
    market_price = models.FloatField()
    sales_num = models.IntegerField()
    store_num = models.IntegerField()


class Cart(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    cart_num = models.IntegerField()
    is_choose = models.BooleanField(default=1)


class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    totalPrice = models.FloatField()
    order_time = models.DateTimeField(auto_now=True)
    order_state = models.IntegerField()  # (default=ORDER_STATE_NO_PAY)


class OrderGoods(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    goods_num = models.IntegerField()
    is_finish = models.BooleanField()


class AfterSale(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    product_name = models.CharField(max_length=200)
    product_question = models.CharField(max_length=500)
    img = models.ImageField()


class Collection(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Goods, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
