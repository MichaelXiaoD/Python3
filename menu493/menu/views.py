# coding=utf-8

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Menu
from . import utils


class MenuListView(generic.ListView):
    model = Menu
    page_kwarg = 'supply_date'
    context_object_name = 'menu_list'
    template_name = 'menu_index.html'

    def get_queryset(self):
        meal = Menu.objects.get(supplyDate__month=7)
        dishs = meal.dishs.all()
        return meal, dishs
