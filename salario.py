valor_da_hora = float(input('Quanto recebe por hora?'))
hora_por_mes = float(input('Quantas horas trabalha no mes?'))
#salario brutro
salario_bruto = (valor_da_hora+hora_por_mes)*30

print('O seu salario é:', salario_bruto)

#desconto do IR 11%
desconto_IR = (salario_bruto*0.11)
print('Desconto de IR:', desconto_IR)
#desconto do inss 8%
desconto_do_inss = (salario_bruto*0.08)
print('Desconto do INSS:', desconto_do_inss)
#sindicato 5%
desconto_sindicato = (salario_bruto*0.05)
print('Desconto do Sindicato:', desconto_sindicato)
#total Descontos
descontos = (desconto_sindicato+desconto_IR+desconto_do_inss)
print('Total de descontos:', descontos)
#salario liquido
salario_liquido = float(salario_bruto-descontos)
print('Seu salário liquido é de:', salario_liquido)