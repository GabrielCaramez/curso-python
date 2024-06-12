import random
alunos = input('informe os alunos separados por virgula: ')
alunos_list = alunos.split(',')
random.shuffle(alunos_list)
print('A ordem de apresentação é {}'.format(alunos_list))