nome = input('Digite seu nome completo: ')
dividir = nome.split()
pnome = dividir[0]
unome = dividir[-1]
print('Primeiro nome: {}'.format(pnome))
print('Ultimo nome: {}'.format(unome))