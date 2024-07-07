from tabulate import tabulate
import defs
import json
import csv

MenuOp = ''
while MenuOp != '4':
    print("\033c", end="")
    # inicia o menu principal
    print('Tabuleiro de Números\n1-Jogar\n2-Tutorial\n3-Ultimos vencedores\n4-Sair do Jogo\n')
    MenuOp = input("Selecione uma opção: ")
    print("\033c", end="")

    match MenuOp:
        case '1':
            InvalidOpGame = True
            while InvalidOpGame:
                # caso exista um jogo, pode iniciar, ou começa um novo jogo
                JogoOp = input("1-Começar novo jogo\n2-Continuar um jogo")
                if JogoOp == '1':
                    print("\033c", end="")
                    print('1-Fácil(3x3)\n2-Média(4x4)\n3-Difícil(5x5)\n')
                    # usa da função para estabelecer as regras do jogo, baseado na dificuldade selecionada
                    tabuleiro, jogadas, indice, tabuleiroStr = defs.dificuldade()
                    InvalidOp = True
                    while InvalidOp:
                        # pergunta se tera jogada especial
                        especial = input('Será jogado com o especial?\n1-Sim 2-Não\nSelecione: ')
                        print("\033c", end="")
                        if especial == '1':
                            InvalidOp = False
                        if especial == '2':
                            InvalidOp = False
                        else:
                            print('Digite um valor valido!')
                    print("\033c", end="")
                    # Sorteia o objetivo do jogador
                    ObPlayerStr1 = defs.objetivo()
                    ObPlayerStr2 = defs.objetivo()
                    # cria-se a lista com o objetivo do player
                    ObPlayer1 = defs.SerieObjetivo(ObPlayerStr1, indice)
                    ObPlayer2 = defs.SerieObjetivo(ObPlayerStr2, indice)
                    # cria lista de listas com todas possibilidades de vitoria do player
                    VitoriaPlayer1 = defs.SerieVencedora(ObPlayerStr1, ObPlayer1, indice)
                    VitoriaPlayer2 = defs.SerieVencedora(ObPlayerStr2, ObPlayer2, indice)

                    # Mostra para os jogadores seus objetivos
                    input("Aperte enter para ver o objetivo do jogador 1")
                    input(f'Seu objetivo é {ObPlayerStr1}(aperte enter e passe para o proximo jogador)')
                    print("\033c", end="")
                    input("Aperte enter para ver o objetivo do jogador 2")
                    input(f'Seu objetivo é {ObPlayerStr2}, aperte enter para começar o jogo')
                    print("\033c", end="")
                    Player = False
                    especial1 = True
                    especial2 = True
                    InvalidOpGame = False

                elif JogoOp == '2':
                    # Caso tenha jogo salvo é perguntado o nome do jogo
                    InvalidOpGame = False
                    nome = input("Digite o nome do jogo salvo que deseja continuar: ")
                    with open(f"{nome}.json") as savefile:
                        game = json.load(savefile)
                    
                    # após isso, recebe todas variaveis salvas do jogo selecionado
                    tabuleiro = game['tabuleiro']
                    Player = game['lastPlayer']
                    especial1 = game['Especial1']
                    especial2 = game['Especial2']
                    VitoriaPlayer1 = game['VitoriaPlayer1']
                    VitoriaPlayer2 = game['VitoriaPlayer2']
                    jogadas = game['jogadas']

                else:
                    print("Digite um valor valido")

            condi = ''
            # Inicia a a partida
            while condi != "2":
                # O Player será configurado sendo: 
                # Player = True é player1
                # Player = False é player2
                Player = not Player
                
                print("\033c", end="")
                if Player:
                    print("\033[0;34;1mVez do Player1\033[m")
                else:
                    print("\033[0;31;1mVez do Player2\033[m")
                
                print(tabulate(tabuleiroStr, headers='firstrow', tablefmt='fancy_grid'))
                game = input("1-jogar\n2-Sair e salvar\n3-Sair sem salvar")
                # Reseta as colunas e linhas ao inicio do looping
                row, col = '', ''
                match game:
                    case '1':
                        if especial == '1':
                            # Caso especial tenha sido habilitado, entra na opção de usar o especial
                                if Player == True and especial1 == True:
                                    # se o player tiver o especial true, ele usará e perderá,
                                    # para ser usado apenas uma vez por partida
                                    InvalidSpecial = True
                                    while InvalidSpecial:
                                        PlayerSpecial = input("1- Limpar coluna\n2- Limpar linha\n3-Não usar especial")
                                        if PlayerSpecial == '1':
                                            tabuleiro, Usoespecial, tabuleiroStr = defs.SpecialCol(tabuleiro, indice, tabuleiroStr)
                                            InvalidSpecial = False

                                        elif PlayerSpecial == '2':
                                            tabuleiro, Usoespecial = defs.SpecialRow(tabuleiro, indice, tabuleiroStr)
                                            InvalidSpecial = False

                                        elif PlayerSpecial == '3':
                                            InvalidSpecial = False
                                        else:
                                            print("Digite um valor valido")
                                    if PlayerSpecial != '3':
                                        especial2 = Usoespecial

                                    especial1 = Usoespecial
                                elif Player == False and especial2 == True:
                                    InvalidSpecial = True
                                    while InvalidSpecial:
                                        PlayerSpecial = input("1- Limpar coluna\n2- Limpar linha\n3-Não usar especial")
                                        if PlayerSpecial == '1':
                                            tabuleiro, Usoespecial, tabuleiroStr = defs.SpecialCol(tabuleiro, indice)
                                            InvalidSpecial = False

                                        elif PlayerSpecial == '2':
                                            tabuleiro, Usoespecial, tabuleiroStr = defs.SpecialRow(tabuleiro, indice)
                                            InvalidSpecial = False

                                        elif PlayerSpecial == '3':
                                            InvalidSpecial = False
                                        else:
                                            print("Digite um valor valido")
                                    if PlayerSpecial != '3':
                                        especial2 = Usoespecial
                                    
                               
                        # Escolhe qual numero sera usado e onde sera posicionado no tabuleiro
                        print(f"Números disponíveis: {jogadas}")
                        num = defs.escolherNumero(jogadas)
                        row, col = defs.escolherPosicao(tabuleiro, indice)
                        if Player:
                            tabuleiroStr[row][col] = f"\033[0;34m{num}\033[m"
                        else:
                            tabuleiroStr[row][col] = f"\033[0;31m{num}\033[m"
                        tabuleiro[row][col] = num
                        jogadas.remove(num)

                        #  Checa se ouve vitoria(isso se repete a cada jogada)
                        Ganhador = defs.CheckVitoria(VitoriaPlayer1, VitoriaPlayer2, Player,tabuleiro, row, col)
                        if Ganhador == 'player1' or Ganhador == 'player2':
                            # caso a vitoria seja de algum player entra na opção de adicionar 
                            # a tabela de vencedores o nome do vencedor 
                            InvalidName = True
                            while InvalidName:
                                print("\033c", end="")
                                print(tabulate(tabuleiroStr, headers='firstrow', tablefmt='fancy_grid'))
                                nomeranking = input(f'Parabens {Ganhador}!!, agora adicione seu nome a tabela de vencedores: ')
                                if nomeranking == '':
                                    print("Digite um nome!")
                                else:
                                    InvalidName = False
                                condi = '2'

                                rakingadd = open('ranking.csv', 'a', newline='')
                        # checa se todas as casas foram preenchidas, caso tenham sido empate sera verdadeiro
                        for i in range(len(tabuleiro)):
                            if '' in tabuleiro[i]:
                                empate = False
                            else:
                                empate = True
                        # caso o empate seja verdadeiro, nenhum jogador vence e o jogo acaba
                        if empate:
                            print(tabulate(tabuleiroStr, headers='firstrow', tablefmt='fancy_grid'))
                            input('EMPATE!! Nenhum jogador atingiu o seu objetivo!(enter para continuar)')
                            condi = '2'
                    
                    case '2':
                        # Salva o jogo caso o player não queira terminar a partida
                        condi = '2'
                        print("\033c", end="")
                        nome = input("Digite um nome para salvar o jogo: ")
                        game = {
                            "tabuleiro": tabuleiro,
                            "lastPlayer": not Player,
                            "Especial1": especial1,
                            "Especial2": especial2,
                            "VitoriaPlayer1": VitoriaPlayer1,
                            "VitoriaPlayer2": VitoriaPlayer2,
                            "jogadas": jogadas
                        }
                        try:
                            gamejson = json.dumps(game)
                            with open(f"{nome}.json", "w") as savefile:
                                savefile.write(gamejson)
                        except:
                            print(IOError)

                    case '3':
                        # Sai do jogo sem salvar
                        condi = '2'          
                        input('saindo do jogo sem salvar...')
        
        case '2':
            # Tutoruial de como jogar o jogo
            print('Como jogar o jogo: Há um tabuleiro que pode ter N por N casas e deve ser jogado por dois jogadores. Cada jogador, em sua vez e de forma alternada, pode selecionar um número dentre os números disponíveis e posicionar este número em uma das casas. Ganha o jogador que fizer a sequência de N números em linha (diagonal, vertical ou horizontal, com leitura da esquerda para a direita e de cima para baixo) que atende ao seu objetivo. O jogo termina em empate se todas as casas do tabuleiro forem marcadas sem que nenhum jogador tenha completado uma sequência de objetivos.')
            input('(enter para voltar ao menu)')
        
        case '3':
            # Mostra a tabela de vencedores
            try:
                print("Tabela com vencedores")
                ranking = open('raking.csv','r',newline='')
                reader = csv.reader(ranking, delimiter=',')
                ranking = [row for row in reader]
                ranking.close()
            except:
                print(IOError)

            print(tabulate(ranking, headers='firstrow', tablefmt='fancy_grid'))
            input("ENTER para voltar para o menu")
            

        case '4':
            # Sai do programa
            print('\nFinalizando programa')
        case _:
            print("Digite uma opção valida")