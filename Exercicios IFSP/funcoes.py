# -*- coding:utf-8 -*-
''' Exemplo de funcao '''
def area_retangulo (base, altura):
    ''' Calcula a area de um triangulo '''
    return base * altura

valor = area_retangulo(10, 5)

lista = ['a', 'aa', 'baa']

''' Exercicio minha resolução ''' 
def maior_string (lista):
    maior = 0
    index = len(lista)
    
    for i in range(0,index):
        if len(lista[i]) > maior:
            maior_index = i

    return lista[maior_index]

#print(maior_string(lista))


''' Exercicio resolucao exemplo '''
def maior_comprimento(lista_str):
    maior = 0
    for i in range(len(lista_str)):
        if len(str(lista_str[i])) > len(str(lista_str[maior])):
            maior = i
    return lista_str[maior]

#print maior_comprimento(lista)


''' Resolução com dicionario desempacotado '''
def maior_comprimento(**kwargs):
    maior_str = ''
    for chave in kwargs:
        if len(str(kwargs[chave])) > len(maior_str):
            maior_str = kwargs[chave]
    return maior_str
dic = {'nome1':'fulano', 'nome2':'Ciclano', 'nome3':'Beltrano'}
print maior_comprimento(**dic)