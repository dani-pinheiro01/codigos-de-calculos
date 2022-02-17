numero=int(input('Digite um valor:'))
x = 1
while x <= 10:

    resultado = x * numero
    print('%d*%d=%d' %(x, numero, resultado))
    x = x + 1
print('Termino da operação.')
