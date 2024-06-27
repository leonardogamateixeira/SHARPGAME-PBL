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




def SerieVencedora(jogadas, indice):
    objetivo = objetivo()
    if objetivo == 'Par':
        lista = [2,4,6,8,10,12,14,16,18,20,22,24]
        listaobjetivo = recorte(lista, indice)
        listareversa = listaobjetivo.reverse()

    elif objetivo == 'Impar':
        lista = [1,3,5,7,9,11,13,15,17,19,21,23,25]
        listaobjetivo = recorte(lista, indice)
        listareversa = listaobjetivo.reverse()

    elif objetivo == 'Crescente':
        lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        listaobjetivo = recorte(lista, indice)

    elif objetivo == 'Decrescente':
        lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25].reverse()
        listaobjetivo = recorte(lista, indice)



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

def vitoria(objetivo1, objetivo2, Player, tabuleiro):
    if objetivo1 == 'Par':
        return False