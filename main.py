import csv
# from tabulate import tabulate
import defs
import json
# oioi
MenuOp = ''
while MenuOp != '4':
    print("\033c", end="")
    print('Tabuleiro de Números\n1-Jogar\n2-Tutorial\n3-Ultimos vencedores\n4-Sair do Jogo\n')
    MenuOp = input("Selecione uma opção: ")
    print("\033c", end="")

    match MenuOp:
        case '1':
            InvalidOpGame = True
            while InvalidOpGame:
                JogoOp = input("1-Começar novo jogo\n2-Continuar um jogo")
                if JogoOp == '1':
                    print("\033c", end="")
                    print('1-Fácil(3x3)\n2-Média(4x4)\n3-Difícil(5x5)\n')
                    tabuleiro, jogadas, indice = defs.dificuldade()
                    InvalidOp = True
                    while InvalidOp:
                        especial = input('Será jogado com o especial?\n1-Sim 2-Não\nSelecione: ')
                        print("\033c", end="")
                        if especial == '1':
                            InvalidOp = False
                        if especial == '2':
                            InvalidOp = False
                        else:
                            print('Digite um valor valido!')
                    print("\033c", end="")

                    ObPlayerStr1 = defs.objetivo()
                    ObPlayerStr2 = defs.objetivo()

                    ObPlayer1 = defs.SerieObjetivo(ObPlayerStr1, indice)
                    ObPlayer2 = defs.SerieObjetivo(ObPlayerStr2, indice)

                    VitoriaPlayer1 = defs.SerieVencedora(ObPlayerStr1, ObPlayer1, indice)
                    VitoriaPlayer2 = defs.SerieVencedora(ObPlayerStr2, ObPlayer2, indice)

                    input("Aperte enter para ver o objetivo do jogador 1")
                    input(f'Seu objetivo é {ObPlayerStr1}(aperte enter e passe para o proximo jogador)')
                    print("\033c", end="")
                    input("Aperte enter para ver o objetivo do jogador 2")
                    input(f'Seu objetivo é {ObPlayerStr2}, aperte enter para começar o jogo')
                    print("\033c", end="")
                    Player = False
                    InvalidOpGame = False

                elif JogoOp == '2':
                    InvalidOpGame = False
                    nome = input("Digite o nome do jogo salvo que deseja continuar: ")
                    with open(f"{nome}.json") as savefile:
                        game = json.load(savefile)
                    
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
            while condi != "2":
                Player = not Player
                print("\033c", end="")
                if Player:
                    print("\033[0;34;1mVez do Player1\033[m")
                else:
                    print("\033[0;31;1mVez do Player2\033[m")
                
                # print(tabulate(tabuleiro, headers='firstrow', tablefmt='fancy_grid'))
                print(tabuleiro)
                game = input("1-jogar\n2-Sair e salvar\n3-Sair sem salvar")
                row, col = '', ''
                match game:
                    case '1':
                        if especial == '1':
                            InvalidSpecial = True
                            while InvalidSpecial:
                                PlayerSpecial = input("1- Limpar coluna\n2- Limpar linha\n3-Não usar especial")
                                if PlayerSpecial == '1':
                                    tabuleiro, especial = defs.SpecialCol(tabuleiro, indice, jogadas)
                                    InvalidSpecial = False
                                elif PlayerSpecial == '2':
                                    tabuleiro, especial = defs.SpecialRow(tabuleiro, indice, jogadas)
                                    InvalidSpecial = False
                                elif PlayerSpecial == '3':
                                    InvalidSpecial = False
                                else:
                                    print("Digite um valor valido")
                            if Player:
                                especial1 = especial
                            else:
                                especial2 = especial

                        print(f"Números disponíveis: {jogadas}")
                        num = defs.escolherNumero(jogadas, tabuleiro, indice)
                        row, col = defs.escolherPosicao(tabuleiro, indice)
                        tabuleiro[row][col] = num
                        Ganhador = defs.CheckVitoria(VitoriaPlayer1, VitoriaPlayer2, Player,tabuleiro, row, col)
                        if Ganhador == 'player1' or Ganhador == 'player2':
                            InvalidName = True
                            while InvalidName:
                                print("\033c", end="")
                                print(tabulate(tabuleiro, headers='firstrow', tablefmt='fancy_grid'))
                                # print(tabuleiro)
                                nomeranking = input(f'Parabens {Ganhador}!!, agora adicione seu nome a tabela de vencedores para eternizar o momento: ')
                                if nomeranking == '':
                                    print("Digite um nome!")
                                else:
                                    InvalidName = False
                                condi = '2'

                        for i in range(len(tabuleiro)):
                            if '' in tabuleiro[i]:
                                empate = False
                            else:
                                empate = True

                        if empate:
                            print(tabuleiro)
                            input('EMPATE!! Nenhum jogador atingiu o seu objetivo!(enter para continuar)')
                            condi = '2'

                    case '2':
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
                        condi = '2'          
                        input('saindo do jogo sem salvar...')
        
        case '2':
            print('Como jogar o jogo: Há um tabuleiro que pode ter N por N casas e deve ser jogado por dois jogadores. Cada jogador, em sua vez e de forma alternada, pode selecionar um número dentre os números disponíveis e posicionar este número em uma das casas. Ganha o jogador que fizer a sequência de N números em linha (diagonal, vertical ou horizontal, com leitura da esquerda para a direita e de cima para baixo) que atende ao seu objetivo. O jogo termina em empate se todas as casas do tabuleiro forem marcadas sem que nenhum jogador tenha completado uma sequência de objetivos.')
            input('(enter para voltar ao menu)')
            # MAIS DETALHES E TABELAS EXEMPLO
        
        case '3':
            # Organizar o arquivo csv e printar a tabela
            print("Tabela com vencedores")
        
        case '4':
            print('\nFinalizando programa')
        case _:
            print("Digite uma opção valida")