from random import randrange
from copy import deepcopy

def dificuldade():
    # o usuario seleciona uma dificuldade, e baseado na resposta, é montado 
    # o tabuleiro e a lista de numeros que podem ser jogados
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
        tabuleiro = [['' for j in range(index)] for i in range(index)]
        tabuleiroStr = deepcopy(tabuleiro)
    return tabuleiro, PlayerNum, index, tabuleiroStr

def objetivo():
    #  sorteia o objetivo do jogador
     lista = ['Par', 'Impar', 'Crescente', 'Decrescente']
     objetivo = lista[randrange(len(lista))]
     return objetivo

def recorte(lista, indice):
    # recebe a lista de numeros que podem ser jogados, e recorta ela para os numeros
    # que podem ser jogados baseados no tamanho do tabuleiro
    match indice:
        case 3:
            return [i for i in lista if i <= 9]
        case 4:
            return [i for i in lista if i <= 16]
        case 5:
            return [i for i in lista if i <= 25]

def SerieObjetivo(objetivo, indice):
    # baseado no objetivo, cria uma lista com os numeros totais do objetivo
    # e recorta a lista baseado no tabuleiro
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

def SpecialRow(tabuleiro, index, tabuleiroStr):
    # Pega a linha selecionada pelo jogador e subistitui todos numeros que tiverem
    # na linha por '' para fazer a jogada especial
    invalidRow = True
    especial = False
    while invalidRow:
        DelRow = int(input(f"Escolha a linha (1-{index}): ")) - 1
        if 0 <= DelRow < index:
            tabuleiro[DelRow] = ['' for i in tabuleiro[index - 1]]
            tabuleiroStr[DelRow] = ['' for i in tabuleiro[index - 1]]
            invalidRow = False
        else:
            print(f"Posição inválida. Escolha entre 1 e {index}.")
    return tabuleiro, especial, tabuleiroStr

def SpecialCol(tabuleiro,index, tabuleiroStr):
    # Pega a coluna selecionada pelo jogador e subistitui todos numeros que tiverem
    # na coluna por '' para fazer a jogada especial
    invalidPos = True
    especial = False
    while invalidPos:
        DelCol = int(input(f"Escolha uma coluna (1-{index}): ")) - 1
        if 0 <= 1 < index:
            for i in range(len(tabuleiro)):
                tabuleiro[i][DelCol] = ''
                tabuleiroStr[i][DelCol] = ''
            invalidPos = False
        else:
            print(f"Posição inválida. Escolha entre 1 e {index}.")
    return tabuleiro, especial, tabuleiroStr

def escolherNumero(jogadas):
    # O jogador digita um numero e a função checa se esse numero está disponivel para ser jogado
    InvalidNum = True
    while InvalidNum:
        num = int(input("Escolha um número para colocar no tabuleiro: "))
        if num in jogadas:
            InvalidNum = False
        else:
            print("escolha um numéro disponivel.")
    return num

def escolherPosicao(tabuleiro, index):
    # Escolhe a linha e a coluna que será posicionada o número
    # e checa se a posicao existe ou ja está ocupada
    invalidPos = True
    while invalidPos:
        row = int(input(f"Escolha a linha (1-{index}): ")) - 1
        col = int(input(f"Escolha a coluna (1-{index}): ")) - 1
        if 0 <= row < index and 0 <= col < index:
            if tabuleiro[row][col] == '':
                invalidPos = False
            else:
                print("Posição já ocupada. Escolha novamente.")
        else:
            print(f"Posição inválida. Escolha entre 1 e {index}.")
    return row, col
  
def SerieVencedora(PlayerStr, ObPlayer, indice):
    # Cria listas de listas com todas as possiveis vitorias do usuario
    # e devolve as sequencias, para serem checadas
    sequencias = []
    for jogada in range(len(ObPlayer)):
        if jogada > len(ObPlayer) - indice:
                return sequencias
        combinacao = []
        combinacao2 = []
        for j in range(indice):
            combinacao.append(ObPlayer[jogada+j])
            combinacao2.append(ObPlayer[jogada+j])
        combinacao2.reverse()
        sequencias.append(combinacao)
        if PlayerStr == 'Par' or PlayerStr == 'Impar':
            sequencias.append(combinacao2)

def CheckRow(objetivo1, objetivo2,tabuleiro, row):
    # Checa se a ultima linha que teve a jogada e observa se algum objetivo foi concluido
    # retorna qual player compriu o objetivo, e caso os dois tenham, retorna empate
    if tabuleiro[row] in objetivo1 and tabuleiro[row] in objetivo2:
        return 'draw'
    if tabuleiro[row] in objetivo1:
        return 'player1'
    if tabuleiro[row] in objetivo2:
        return 'player2'
    

def CheckCol(objetivo1, objetivo2,tabuleiro, col):
    # Checa se a ultima coluna que teve a jogada e observa se algum objetivo foi concluido
    # retorna qual player compriu o objetivo, e caso os dois tenham, retorna empate
    coluna = [row[col] for row in tabuleiro]
    if coluna in objetivo1 and coluna in objetivo2:
        return 'draw'
    if coluna in objetivo1:
        return 'player1'
    if coluna in objetivo2:
        return 'player2'

def CheckDiagonal(objetivo1, objetivo2,tabuleiro):
    # Checa se a ultima diagonal que teve a jogada e observa se algum objetivo foi concluido
    # retorna qual player compriu o objetivo, e caso os dois tenham, retorna empate
    diagonalcres = [tabuleiro[indice][indice] for indice in range(len(tabuleiro))]
    diagonaldec = [tabuleiro[-(indice+1)][indice] for indice in range(len(tabuleiro))]
    if (diagonalcres in objetivo1 or diagonaldec in objetivo1) and (diagonalcres in objetivo2 or diagonaldec in objetivo2):
        return 'draw'
    if (diagonalcres in objetivo1 or diagonaldec in objetivo1):
        return 'player1'
    if (diagonalcres in objetivo2 or diagonaldec in objetivo2):
        return 'player2'

def CheckVitoria(objetivo1, objetivo2, Player, tabuleiro, row, col):
    # Observa qual player ganhou e adiciona a variavel ganhador, caso tenha
    # retornado empate, o player que fez a ultima jogada para concluir o objetivo ganha
    ganhador = None
    ganhouDig = CheckDiagonal(objetivo1, objetivo2, tabuleiro)
    if ganhouDig == 'player1' or ganhouDig == 'player2':
        ganhador = ganhouDig

    ganhouRow = CheckRow(objetivo1, objetivo2, tabuleiro, row)
    if ganhouRow == 'player1' or ganhouRow == 'player2':
        ganhador = ganhouRow

    ganhouCol = CheckCol(objetivo1, objetivo2, tabuleiro, col)
    if ganhouCol == 'player1' or ganhouCol == 'player2':
        ganhador = ganhouCol

    if ganhouCol == 'draw' or ganhouRow == 'draw' or ganhouDig == 'draw':
        if Player: ganhador = 'player1'
        else: ganhador = 'player2'

    if ganhador != None:
        return ganhador