cigarro = int(input('digite quantas vezes por dia vc usa o cigarro '))
ano = float(input('digite quantos anos vc usa o fumo '))
mult = cigarro * 365.25 * ano * 10 / 60 / 24
print('o valor em dias perdidos foi de: {}'.format(mult))