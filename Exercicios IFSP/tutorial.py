# -*- coding:utf-8 -*-
print ('Hello World!')

'''
Coleções de objetos
'''
lista = [10, 20, 30, 40]
lista.append(100) #adiciona valores
lista.pop(1) # remove valores
print(lista)
print(lista[1])


# Criando uma lista de impares
lista_impares = []

for i in range(1,101):
    if i % 2 == 1:
        lista_impares.append(i)
# metodo inline
lista_imp = [i for i in range(1,101) if 1 % 2 == 1]

dicionario = {1:'a', 2:'b', 3:'c'}
print(dicionario)

# Criando dicionario dinamicamente
dic = {str(i): i for i in lista_impares}
print(dic)

