"""Математические функции"""
import math


def quadrat(num):
    return num ** 2


def cub(num):
    return num ** 3


def coren(num):
    return math.sqrt(num)


def modul(num):
    return abs(num)


def sinus(num):
    return math.sin(num)


mydict = {"квадрат": quadrat, "модуль": modul, "куб": cub, "корень": coren, "синус": sinus}

num = int(input())
func = input()

print(mydict[func](num))


