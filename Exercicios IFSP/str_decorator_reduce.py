# -*- coding:utf-8 -*-

'''
    Reduce facilita a passagem de parametros
    semelhante a um comportamento recursivo
    @todo: estudar a REDUCE
'''

def str_decorator(func):
    def wrapper(*args):
        return str(reduce(func, args))
    return wrapper

@str_decorator
def soma(n1, n2):
    return n1 + n2

print(soma(1, 2, 3, 4))