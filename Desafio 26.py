p = str(input('Digite uma frase: '))
p = p.lower()
ca = p.count('a')
fa = p.find('a')
fl = p.rfind('a')
print('A letra A aparece {} vezes na frase'.format(ca))
print('Sua frase tem pela primeira a letra A na posição {}'.format(fa))
print('Sua frase tem pela ultima vez a palavra A na posição {}'.format(fl))