notas = []
marcaçao = 1

escolha = int(input('[1] Informe as notas [-1] Sair \nQual a sua escolha? '))
if escolha == 1:
    while True:
        nota_1 = float(input(f'digite {marcaçao} a nota:'))
        if nota_1 == -1:
            break
        notas.append(nota_1)
        marcaçao += 1
print('Fim da Linha')


quantidade = len(notas)
inverso = notas[::-1]
soma = sum(notas)
media = soma/quantidade
acimamedia = len([n for n in notas if n >= media])
menorque7 = len([n for n in notas if n < 7])


print(f'{quantidade} Valores lidos')

print(f'Ordém das notas:{notas}')

print(f'A soma das notas:{soma}')

print(f'A média das notas:{media}')

print(f'Notas acima da média:{acimamedia}')

print(f'Notas abaixo de 7:{menorque7}')

print('Obrigado por usar meu programa!!')