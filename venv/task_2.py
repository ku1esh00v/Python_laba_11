#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def circle(radius):
    return math.pi * radius ** 2


def cylinder():
    radius = float(input("Введите радиус основания цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    choice = input("Хотите ли вы получить только площадь боковой поверхности цилиндра? (да/нет): ")

    if choice.lower() == "да":
        side_area = 2 * math.pi * radius * height
        print("Площадь боковой поверхности цилиндра:", side_area)
    else:
        side_area = 2 * math.pi * radius * height
        full_area = side_area + 2 * circle(radius)
        print("Полная площадь цилиндра:", full_area)


cylinder()
