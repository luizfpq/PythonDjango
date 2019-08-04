# -*- coding: utf-8 -*-
'''
@author: LuizQuirino 
@contact: luizfpq@gmail.com

Exercício 1
Pedir ao usuário para informar o valor de três
valores numéricos e calcular a média
'''
val1 = float(input('Entre com o primeiro valor: '))
val2 = float(input('Entre com o segundo valor: '))
val3 = float(input('Entre com o terceiro valor: '))

media = (val1 + val2 + val3) / 3

print('A media dos tres valores inseridos é: {}'.format(media))