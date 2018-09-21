##优惠卷
from weixin.models import Weixin_user
from weixin.models import Coupon

from django.utils import timezone
import pdb

###test
def login_test(open_id):
    obj = Weixin_user(openid=open_id)
    obj.save()
    print(obj.id)

####注册时给用户添加优惠卷
def login_add_coupon(openid):
    user = Weixin_user.objects.get(openid=openid)
    user.coupon_set.create(price='login',state=1,start_time=timezone.now())
    user.coupon_set.create(price='share_once',state=1,start_time=timezone.now())
    user.coupon_set.create(price='share_twice',state=1,start_time=timezone.now())
    print(user.coupon_set.count())

def run():
    #login_add('test1'+str(1234))
    login_add_coupon('test')