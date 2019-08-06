# -*- coding:utf-8 -*-
'''
@author: LuizQuirino
@contact: luizfpq@gmail.com

Exercício 3

Escreva um programa que leia do usuário o nome e RA de 3 alunos e armazene essa
informação em um dicionário, relacionando o RA ao nome do aluno

Peça ao usuário para informar um RA e exiba o nome do aluno associado

'''
from soupsieve.util import string

user1 = raw_input('Entre com o RGA do aluno 1: ')
userName1 = raw_input('Entre com nome do aluno 1: ')

user2 = raw_input('Entre com o RGA do aluno 2: ')
userName2 = raw_input('Entre com nome do aluno 2: ')

user3 = raw_input('Entre com o RGA do aluno 3: ')
userName3 = raw_input('Entre com nome do aluno 3: ')

students = {user1:userName1, user2:userName2, user3:userName3}

find = raw_input('Informe um RGA para buscar:')

print('O aluno pesquisado é: {}'.format(students[find]))