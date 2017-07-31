# coding=utf-8

from django.http import HttpResponse, HttpRequest, JsonResponse
from .utils import date_deprocess, time_deprocess
from django.core.serializers import serialize
from json import JSONDecoder
from .models import Menu


def menulist_page(request):
    supply_date = request.GET.get('supply_date')
    time = request.GET.get('time')
    meal = Menu.objects.get(supplyDate=date_deprocess(supply_date), supplyTime=time_deprocess(time))
    menu_dishs = serialize('json', meal.dishs.all())
    jsonRes = JsonResponse({
        'menu_supply_date': meal.supplyDate,
        'menu_time': meal.supplyTime,
        'menu_dishs': JSONDecoder().decode(menu_dishs)
    })
    return jsonRes
