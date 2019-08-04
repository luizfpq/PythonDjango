# -*- coding: utf-8 -*-
'''
@author: LuizQuirino
@contact: luizfpq@gmail.com

Exercício 2

Considere a lista de funcionários de uma empresa
engenheiros → [Joao, Nice, Sueli, Amanda]
programadores → [Joao, Sofia, Rafael, Amanda]
gerentes → [Nice, Sueli, Rafael, Joao]
– Usando Sets, imprima o nome de todos os funcionários da empresa
– Crie e imprima o set dos funcionários que são engenheiros e programadores
– Crie e imprima o set dos programadores e gerentes
'''

eng = {'Joao', 'Nice', 'Sueli', 'Amanda'}
prog = {'Joao', 'Sofia', 'Rafael', 'Amanda'}
ger = {'Nice', 'Sueli', 'Rafael', 'Joao'}

all = eng | prog | ger
ep = eng & prog
pg = prog & ger

print('Todos os funcionarios: {}'.format(all))
print('Engenheiros e programadores: {}'.format(ep))
print('Programadores e gerentes: {}'.format(pg))  