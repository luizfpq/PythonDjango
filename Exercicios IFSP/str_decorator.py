# -*- coding:utf-8 -*-

def str_decorator(func):
    def wrapper(n1, n2):
        return str(func(n1, n2))
    return wrapper

@str_decorator
def soma(n1, n2):
    return n1 + n2

print(soma(1, 2))