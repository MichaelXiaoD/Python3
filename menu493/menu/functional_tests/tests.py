# coding=utf-8

from datetime import date, time
from django.urls import reverse
from django.test import TestCase

from ..utils import date_process, time_process
from ..models import Menu, Dish
from json import JSONDecoder

# 用户肖盾在上午10点，他登陆了微信小程序，小程序首先提交了用户验证，

# 小程序发现肖盾是新用户
class NewVisitorView(TestCase):
    def setUp(self):
        timeMorning = time(10)
        self.dateString = date_process(date.today())
        self.timeString = time_process(timeMorning)

        Dish.objects.create(name='手撕兔', type='Meat', price=1.0)
        Dish.objects.create(name='烤鱼', type='Meat', price=1.0)
        menu = Menu.objects.create(supplyDate=date.today(), supplyTime='lunch')
        dishs = Dish.objects.all()
        menu.dishs.add(*dishs)
        url = reverse('menu:menu_list')
        self.response = self.client.get(url, {'supply_date': self.dateString, 'time': self.timeString})

    # 因此小程序显示主页时只是单纯地请求当天的菜单信息
    def test_can_get_the_correct_menu_list(self):
        # 小程序的请求得到了正常响应
        self.assertEqual(self.response.status_code, 200)
        self.assertIn('application/json', str(self.response))
        # 肖盾看了下时间，现在是上午10点，显示的是中餐内容，日期是今天的日期
        result = self.response.json()
        print(result)
        self.assertEqual(self.dateString, result['menu_supply_date'])
        self.assertEqual(result['menu_time'], 'lunch')

    def test_context_of_menu_list_correct(self):
        result = self.response.json()
        self.assertIn('手撕兔', str(result))
        # 他注意到菜单中有荤菜，素菜和套餐，数量分别为11，2，6，总数19。
        self.assertEqual(len(result['menu_dishs']), 19)
        # 他还注意到每道菜都有菜名价格，菜名不重复
        # 他想看的其实是第二天的内容，因此他选择了看第二天中餐的菜单

# 他开始点餐，系统提示他需要先注册
# 他跳转到注册页面开始注册
# 注册完他开始点餐，提交了自己的需求
