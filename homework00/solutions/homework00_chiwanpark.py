# -*- coding: utf-8 -*-

def add_1(xs):
    return [x + 1 for x in xs]


def square(xs):
    return [x ** 2 for x in xs]


def squared_mean(xs):
    return sum((x ** 2 for x in xs)) / len(xs)
