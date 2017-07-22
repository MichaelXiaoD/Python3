# coding=utf-8

from django.db import models
from datetime import date


# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=40, db_column='name')
    type = models.CharField(max_length=10, db_column='type')
    price = models.FloatField(db_column='price', null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    supplyDate = models.DateField(db_column='supply_date', default=date.today())
    supplyTime = models.CharField(max_length=10, db_column='supply_time', default='lunch')
    dishs = models.ManyToManyField(Dish)

    # The __str__() method is called whenever you call str() on an object.
    # Most notably, to display an object in the Django admin site and as the value
    # inserted into a template when it displays an object.
    def __str__(self):
        return '{0} {1}'.format(self.supplyDate, self.supplyTime)
        # return '{0}'.format(self.dishs.name)
