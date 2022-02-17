#As Organizações Tabajara resolveram dar um aumento de salário aos seus
#colaboradores e lhe contraram para desenvolver o programa que calculará os
#.
#Faça um programa que recebe o salário de um colaborador e o reajuste
salario = float(input('Insira o salário do colaborador:'))
#segundo o seguinte critério, baseado no salário atual:
#o salários até R$ 280,00 (incluindo) : aumento de 20%
if (salario <= 280.00):
    percentual = 20
#o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
elif (salario >= 280.00 <=700.00):
    percentual = 15
#o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
elif (salario >= 700.00  <= 1500.00):
    percentual = 10
#o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser
if (salario >= 1500.00):
    percentual = 5

percentual = percentual / 100.0
aumento = percentual * salario
novo_salario = salario + aumento
#realizado, informe na tela:
#o o salário antes do reajuste;
print('O seu salário era:', salario)
#o o percentual de aumento aplicado;
print('O aumento foi de:', percentual)
#o o valor do aumento;
print('O seu aumento foi de:', aumento)
#o o novo salário, após o aumento.
print('O seu novo salário é:', novo_salario)