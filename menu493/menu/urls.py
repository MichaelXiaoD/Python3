# coding=utf-8

from django.conf.urls import url

from . import views

app_name = 'menu'
urlpatterns = [

    #  as_view(): Any positional and/or keyword arguments captured from the URL pattern
    #  are assigned to the args and kwargs attributes, respectively.
    # Then dispatch() is called.
    url(r'^menulist/supply_date=(?P<supply_date>[0-9]{4}-[0-9]{2}-[0-9]{2})&time=(?P<time>[0-9]+)/$',
        views.MenuListView.as_view(), name='menu_list'),
]
