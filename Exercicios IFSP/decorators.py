# -*- coding:utf-8 -*-

def meu_decorator(func):
    def wraper():
        print('Aantes')
        func()
        print('Depois')
    return wraper

def outra_funcao():
    print('Teste')
    
    outra_funcao = meu_decorator(outra_funcao)
    outra_funcao()
    
# outra maneira

@meu_decorator
def outra_funcao():
    print('Teste')
    

    outra_funcao()