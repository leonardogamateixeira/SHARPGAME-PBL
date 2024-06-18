from random import randrange

def dificult(dificultOp):
    invalidop = True
    while invalidop:
        if dificultOp == '1':
                invalidop = False
                index = 3
                PlayerNum = [1,2,3,4,5,6,7,8,9]
        elif dificultOp == '2':
            invalidop = False
            index = 4
            PlayerNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        elif dificultOp == '3':
            invalidop = False
            index = 5
            PlayerNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        else:
            print('Digite um valor valido!')
        tabuleiro = []
        for i in range(0, index):
            row = []
            for j in range(0, index):
                 row.append('')
            tabuleiro.append(row)
    return tabuleiro, PlayerNum

def objetivo():
     lista = ['Par', 'Impar', 'Crescente', ' Decrescente']
     condit = lista[randrange(len(lista))]
     return condit