import csv
from tabulate import tabulate
import defs

MenuOp = ''
while MenuOp != '5':
    print('Tabuleiro de Números\n1-Jogar\n2-Tutorial\n3-Ultimos vencedores\n4-Desabilitar Som\n5-Sair do Jogo\n')
    MenuOp = input("Selecione uma opção: ")
    print("\033c", end="")

    match MenuOp:
        case '1':
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
            VitoriaPlayer1 = defs.SerieVencedora(ObPlayer1, indice)
            VitoriaPlayer2 = defs.SerieVencedora(ObPlayer2, indice)

            input("Aperte enter para ver o objetivo do jogador 1")
            input(f'Seu objetivo é {ObPlayerStr1}(aperte enter e passe para o proximo jogador)')
            print("\033c", end="")
            input("Aperte enter para ver o objetivo do jogador 2")
            input(f'Seu objetivo é {ObPlayerStr2}, aperte enter para começar o jogo')
            print("\033c", end="")

            # Estabelecer condições de vitória
            # fazer o loop do jogo, e as jogadas
            condi = ''
            Player = False
            while condi != "2":
                Player = not Player
                print("\033c", end="")
                print(tabulate(tabuleiro, headers='firstrow', tablefmt='fancy_grid'))
                game = input("1-jogar\n2-Sair e salvar\n3-Sair sem salvar")
                row, col = '', ''
                match game:
                    case '1':
                        if especial == '1':
                            PlayerSpecial = input("1- Deletar uma coluna\n2- Deletar linha\n3-Não usar especial")
                        print(f"Números disponíveis: {jogadas}")
                        num = defs.escolherNumero(jogadas)
                        row, col = defs.escolherPosicao(tabuleiro, indice)
                        tabuleiro[row][col] = num
                        jogadas.remove(num)
                        Ganhador = defs.CheckVitoria(VitoriaPlayer1, VitoriaPlayer2, Player,tabuleiro, row, col)
                        if Ganhador:
                            InvalidName = True
                            while InvalidName:
                                nomeranking = input(f'Parabens {Ganhador}!!, agora adicione seu nome a tabela de vencedores para eternizar o momento: ')
                                if nomeranking == '':
                                    print("Digite um nome!")
                                else:
                                    InvalidName = False
                            with open('ranking.csv', 'a') as rankingfile:
                                csv.writer(rankingfile, delimiter=',').writerow([nomeranking])
                            condi = '2'
                    case '2':
                        condi = '2'
                        input('salvar e sair')
                    case '3':
                        condi = '2'          
                        input('sair e fds')
        
        case '2':
            print('Como jogar o jogo: Há um tabuleiro que pode ter N por N casas e deve ser jogado por dois jogadores. Cada jogador, em sua vez e de forma alternada, pode selecionar um número dentre os números disponíveis e posicionar este número em uma das casas. Ganha o jogador que fizer a sequência de N números em linha (diagonal, vertical ou horizontal, com leitura da esquerda para a direita e de cima para baixo) que atende ao seu objetivo. O jogo termina em empate se todas as casas do tabuleiro forem marcadas sem que nenhum jogador tenha completado uma sequência de objetivos.')
            input('(enter para voltar ao menu)')
            # MAIS DETALHES E TABELAS EXEMPLO
        
        case '3':
            # Organizar o arquivo csv e printar a tabela
            print("Tabela com vencedores")
            with open('ranking.csv', 'r') as rankingfile:
                rankingfile.read()

        case '4':
            print('Desabilitar')
            # desabilitar som e reabilitar, na msm opção
        
        case '5':
            print('\nFinalizando programa')
        case _:
            print("Digite uma opção valida")