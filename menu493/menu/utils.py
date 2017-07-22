# coding=utf-8

from datetime import date, time
import re


def date_process(dateObject):
    year = dateObject.year
    month = dateObject.month
    day = dateObject.day
    s = '{0:#04}-{1:#02}-{2:#02}'.format(year, month, day)
    return s


def time_process(timeObject):
    hour = str(timeObject.hour)
    return hour


def date_deprocess(dateString):
    match = dateString.split('-')
    year = match[0]
    month = match[1]
    day = match[2]
    supplyDate = date(int(year), int(month), int(day))
    return supplyDate


def time_deprocess(timeString):
    time_original = time(int(timeString))
    if 0 < time_original.hour < 13:
        supply_time = 'lunch'
    else:
        supply_time = 'dinner'
    return supply_time
