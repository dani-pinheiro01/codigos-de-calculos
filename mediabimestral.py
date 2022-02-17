matricula = int(input('Digite a matricula do aluno:'))

while (matricula>0):

    nota1 = float(input('Digite a nota da avaliação 1:'))
    nota2 = float(input('Digite a nota da avaliação 2:'))
    faltas = int(input('Digite as faltas do aluno:'))

    media = (nota1*2+nota2*3)/5
    pres = (float)(80-faltas)*100/80

    print('LISTA DE DADOS DO ALUNO')

    print('Média final:', media)
    print('Percentual de presença:', pres)

if media >=6 and pres >=75:
    print('Resultado final: APROVADO')
if media <6 and pres >75:
    print('Resultado final: REPROVADO POR MÉDIA')
if media >=6 and pres <75:
    print('Resultado final: REPROVADO POR FALTA')
if media <6 and pres <75:
    print('Resultado final: REPROVADO POR MÉDIA E FALTAS')

