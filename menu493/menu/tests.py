# coding=utf-8

from django.test import TestCase
from django.urls import reverse
from datetime import date, time

from .models import Menu, Dish
from . import utils

# Create your tests here.
class MenuRequestTests(TestCase):
    def test_menu_request_for_today_morning(self):
        supplyDate = date.today()
        timeMorning = time(10)

        # 新建dish
        str1 = '手撕兔'.encode('UTF-8')
        str2 = '烤鱼'.encode('UTF-8')
        Dish.objects.create(name=str1, type='Meat', price=1.0)
        Dish.objects.create(name=str2, type='Meat', price=1.0)
        menu = Menu.objects.create(supplyDate=supplyDate, supplyTime='lunch')

        dishs = Dish.objects.all()
        print(dishs)

        menu.dishs.add(*dishs)

        menu_get = Menu.objects.get(supplyDate=supplyDate, supplyTime='lunch')
        print(menu_get.dishs)

        # 生成请求体：日期时间处理
        dateString = utils.date_process(supplyDate)
        timeString = utils.time_process(timeMorning)

        # 请求url:/menu_list，参数为supply_date和time: The test client is a Python class that acts as a dummy Web browser
        url = reverse('menu:menu_list', kwargs={'supply_date': dateString, 'time': timeString})
        self.assertEqual(url, '/menu/menulist/supply_date={}&time={}/'.format(dateString, timeString))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['menu_list'],
                                 ['<Menu: {0} lunch>'.format(supplyDate), '<QuerySet [<Dish: 手撕兔>, <Dish: 烤鱼>]>'])


class UtilsTest(TestCase):
    def test_date_process(self):
        dateTest = date(2017, 3, 6)
        result = utils.date_process(dateTest)
        self.assertEqual(result, '2017-03-06')

    def test_time_process(self):
        timeTest = time(9)
        self.assertEqual(utils.time_process(timeTest), '9')

    def test_date_deprocess(self):
        dateString = '2017-04-23'
        self.assertEqual(utils.date_deprocess(dateString), date(2017, 4, 23))

    def test_time_deprocess(self):
        timeString = '11'
        self.assertEqual(utils.time_deprocess(timeString), 'lunch')
