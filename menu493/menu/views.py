# coding=utf-8

from django.http import HttpResponse, HttpRequest, JsonResponse
from .utils import date_deprocess, time_deprocess

from .models import Menu


def menulist_page(request):
    supply_date = request.GET.get('supply_date')
    time = request.GET.get('time')
    meal = Menu.objects.get(supplyDate=date_deprocess(supply_date), supplyTime=time_deprocess(time))
    dishs = meal.dishs.all()
    response = HttpResponse([meal, dishs])
    return response
