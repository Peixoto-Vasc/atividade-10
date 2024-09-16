# Crie um programa que receba um número inteiro e informe se ele é par ou ímpar.

numero = int(input('Digite o numero :'))
resultado = numero % 2
if resultado == 0:
    print('par')
else:
    print('impar')
