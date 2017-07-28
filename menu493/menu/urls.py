# coding=utf-8

from django.conf.urls import url

from . import views

app_name = 'menu'
urlpatterns = [

    #  as_view(): Any positional and/or keyword arguments captured from the URL pattern
    #  are assigned to the args and kwargs attributes, respectively.
    # Then dispatch() is called.
    url(r'^menulist/$',
        views.menulist_page, name='menu_list'),
]
