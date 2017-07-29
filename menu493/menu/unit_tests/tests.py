# coding=utf-8

from django.test import TestCase
from datetime import date, time
from .. import utils


# Create your tests here.

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
