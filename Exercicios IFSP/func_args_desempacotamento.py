# -*- coding:utf-8 -*-

lista = [1,2,3,4]

def soma(n1, n2, *lista):
    resultado = n1 + n2
    for n in lista:
        resultado = n + resultado
    return resultado

print(soma(*lista))