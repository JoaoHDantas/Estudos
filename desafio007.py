materia1 = float(input('Nota da mateira 1: '))
materia2 = float(input('Nota da mateira 2: '))
materia3 = float(input('Nota da meteria 3: '))
soma = (materia1 + materia2 + materia3) // 3
aprovado = soma >= 7
print('Sua media foi de {}'.format(soma))
print('Você foi aprovado: {}'.format(aprovado))
if aprovado == True:
    print('Meus parabéns voce foi aprovado com sucesso ;)')