# -*- coding:utf-8 -*-

try:
    altura = float(raw_input('Digite a altura: '))
    peso   = float(raw_input('Digite o peso: '))
    imc = peso / (altura**2)
    print ('O IMC é: {}'.format(imc))
    if imc < 1:
        raise Exception('IMC menor que um')
except ZeroDivisionError:
    print('Altura não pode ser zero')
except ValueError:
    print('Digite apenas numeros')
    