while True:
    cato = float(input('Digite o cateto oposto: '))
    cata = float(input('Digite o cateto adjacente: '))
    calc = (cato**2 + cata**2)
    hipo = calc**(1/2)
    print(f'A hipotenusa é {hipo:.2f}')
