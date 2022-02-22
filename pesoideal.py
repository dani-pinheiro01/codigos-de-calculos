sexo = input('Qual seu sexo? Masculino(M) ou Feminino(F):')
altura = input('Qual sua altura?')

peso_ideal_M = (72.7*float(altura))-58
peso_ideal_F = (62.1*float(altura))-44.7

if sexo == 'M':
    print('Seu peso ideal é:', peso_ideal_M)

if sexo == 'F':
    print('Seu peso ideal é:', peso_ideal_F)

else:
    print('Sexo invalido')
