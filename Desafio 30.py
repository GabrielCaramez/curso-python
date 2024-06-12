numero = int(input('Digite seu némero pode ser qualquer numero inteiro: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} é Par'.format(numero))
else:
    print('O numero {} é Ímpar'.format(numero))
