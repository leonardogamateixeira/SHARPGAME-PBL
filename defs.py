from random import randrange

def dificuldade():
    invalidop = True
    while invalidop:
        dificultOp = input('Selecione uma dificuldade: ')
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
        # tabuleiro = [['']*index]*index
        tabuleiro = [['' for j in range(index)] for i in range(index)]
    return tabuleiro, PlayerNum, index

def objetivo():
     lista = ['Par', 'Impar', 'Crescente', 'Decrescente']
     objetivo = lista[randrange(len(lista))]
     return objetivo

def recorte(lista, indice):
    match indice:
        case 3:
            return [i for i in lista if i <= 9]
        case 4:
            return [i for i in lista if i <= 16]
        case 5:
            return [i for i in lista if i <= 25]

def SerieObjetivo(objetivo, indice):

    if objetivo == 'Par':
        lista = [2,4,6,8,10,12,14,16,18,20,22,24]
        listaobjetivo = recorte(lista, indice)

    elif objetivo == 'Impar':
        lista = [1,3,5,7,9,11,13,15,17,19,21,23,25]
        listaobjetivo = recorte(lista, indice)

    elif objetivo == 'Crescente':
        lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        listaobjetivo = recorte(lista, indice)

    elif objetivo == 'Decrescente':
        lista = [25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
        listaobjetivo = recorte(lista, indice)
        
    return listaobjetivo

def escolherNumero(jogadas):
    while True:
        num = int(input("Escolha um número para colocar no tabuleiro: "))
        if num in jogadas:
            return num
        else:
            print("Número não disponível.")

def escolherPosicao(tabuleiro, index):
    while True:
        row = int(input(f"Escolha a linha (1-{index}): ")) - 1
        col = int(input(f"Escolha a coluna (1-{index}): ")) - 1
        if 0 <= row < index and 0 <= col < index:
            if tabuleiro[row][col] == '':
                return row, col
            else:
                print("Posição já ocupada. Escolha novamente.")
        else:
            print(f"Posição inválida. Escolha entre 1 e {index}.")
  
def SerieVencedora(ObPlayer, indice):
    sequencias = []
    for jogada in range(len(ObPlayer)):
        if jogada > len(ObPlayer) - indice:
            sequenciasreversa = sequencias[::-1]
            sequencias.extend(sequenciasreversa)
            return sequencias
        combinacao = []
        for j in range(indice):
            combinacao.append(ObPlayer[jogada+j])
        sequencias.append(combinacao)

def CheckRow(objetivo1, objetivo2,tabuleiro, row):
    if tabuleiro[row] in objetivo1 and tabuleiro[row] in objetivo2:
        return 'draw'
    if tabuleiro[row] in objetivo1:
        return 'p1'
    if tabuleiro[row] in objetivo2:
        return 'p2'
    

def CheckCol(objetivo1, objetivo2,tabuleiro, col):
    coluna = [row[col] for row in tabuleiro]
    if coluna in objetivo1 and coluna in objetivo2:
        return 'draw'
    if coluna in objetivo1:
        return 'p1'
    if coluna in objetivo2:
        return 'p2'

def CheckDiagonal(objetivo1, objetivo2,tabuleiro, row):
    diagonalcres = [tabuleiro[indice][indice] for indice in range(len(tabuleiro))]
    diagonaldec = [tabuleiro[-(indice+1)][indice] for indice in range(len(tabuleiro))]
    if (diagonalcres in objetivo1 or diagonaldec in objetivo1) and (diagonalcres in objetivo2 or diagonaldec in objetivo2):
        return 'draw'
    if (diagonalcres in objetivo1 or diagonaldec in objetivo1):
        return 'p1'
    if (diagonalcres in objetivo2 or diagonaldec in objetivo2):
        return 'p2'

def CheckVitoria(objetivo1, objetivo2, Player, tabuleiro, row, col):
    if row == col or -row == col:
        ganhouDig = CheckDiagonal(objetivo1, objetivo2, tabuleiro, row)
        if ganhouDig == 'draw':
            return Player
        else:
            ganhador = ganhouDig

    ganhouRow = CheckRow(objetivo1, objetivo2, tabuleiro, row)
    if ganhouRow == 'draw':
        return Player
    else:
        ganhador = ganhouRow

    ganhouCol = CheckCol(objetivo1, objetivo2, tabuleiro, col)
    if ganhouCol == 'draw':
        return Player
    else:
        ganhador = ganhouCol