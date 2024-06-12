import math
ang = float(input('Digite o angulo que deseja saber o seno cosseno e tangente: '))
ang1 = math.radians(ang)
seno = math.sin(ang1)
cose = math.cos(ang1)
tang = math.tan(ang1)
print('Como o angulo de {}°, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang, seno, cose, tang))