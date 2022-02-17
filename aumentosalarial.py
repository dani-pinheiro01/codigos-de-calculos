salario = float(input('Insira o salário do colaborador:'))

if (salario <= 280.00):
    percentual = 20
elif (salario >= 280.00 <= 700.00):
    percentual = 15
elif (salario >= 700.00  <= 1500.00):
    percentual = 10
if (salario >= 1500.00):
    percentual = 5
    
percentual = percentual / 100.0
aumento = percentual * salario
novo_salario = salario + aumento

print('O seu salário era:', salario)
print('O aumento foi de:', percentual)
print('O seu aumento foi de:', aumento)
print('O seu novo salário é:', novo_salario)
