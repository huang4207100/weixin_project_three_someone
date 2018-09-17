from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Weixin_user(models.Model):
    openid = models.CharField(max_length=50,unique=True)             #微信用户的openid
    start_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Account_info(models.Model):
    weixin_user = models.ForeignKey(Weixin_user,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)             #账号的手机号
    password = models.CharField(max_length=50) #账户的密码

class Class_info(models.Model):
    account_info = models.ForeignKey(Account_info,on_delete=models.CASCADE) #课程的账号
    class_name = models.CharField(max_length=50)    #课程的名字
    class_percent = models.IntegerField(default=0,validators=[MaxValueValidator(100),MinValueValidator(0)]) #课程的百分比

class Order_info(models.Model):
    state_choice = (
        ("CLOSE","已取消"),
        ("GENERATE","已生成"),
        ("PAY","已付款"),
    )
    account_info = models.ForeignKey(Account_info,on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)                         #生成的时间
    update_time = models.DateTimeField(auto_now=True)                            #更新时间
    state = models.CharField(max_length=50,choices=state_choice,default="CLOSE") #订单的状态
    price = models.FloatField(default=9.9)                                       #订单的最终价格
    generate_info = models.CharField(max_length=1000)                            #上传的刷课数据，后面用于导出

class Coupon(models.Model):
    weixin_user = models.ForeignKey(Weixin_user,on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)  #订单生成时间
    price_choice = (
        ("login","29-5"),
        ("share_once","99-19"),
        ("share_twice","149-39"),
    )
    price = models.CharField(max_length=20,choices=price_choice)  #3中订单的状态