# -*- coding: utf-8 -*-
#
# valor1 = float(input('digite o valor 1:'))
# valor2 = float(input('digite o valor 2:'))
#
# soma = valor1 + valor2
# subtracao = valor1 - valor2
# divisao = valor1 / valor2
# resto_da_divisao = valor1 % valor2
# media = (valor1 + valor2)/2
# multiplicacao = valor1 * valor2
#
# print(soma)
# print(subtracao)
# print(divisao)
# print(resto_da_divisao)
# print(media)
# print(multiplicacao)
nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))

if idade >= 18:
    print(f'pode entrar {nome}')

elif idade < 11:
    print(f'menor de idade, voce eh crianca {nome}')

else:
    print('menor de idade')
