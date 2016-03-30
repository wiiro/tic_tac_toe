# -*- coding: cp1252 -*-
'''
Jogo da Velha
1ª versão: duas pessoas, uma contra a outra
2ª versão: uma pessoa contra a máquina
            pergunta se jogador quer jogar com X ou O,
            se joga primeiro ou não

Valida se a posição escolhida está ocupada ou não
Quando um dos lados ganhar, o programa deve avisar quem foi

Validar se alguma linha, coluna ou diagonal está com o mesmo valor

Forma de fazer:
    Tabuleiro: variável "Velha" - iniciar vazio
        Velha = [[ " ", " "," "],[ " ", " "," "],[ " ", " "," "]]
    Para desenhar quadro, função ExibeJogo
        linha = "+----+-----+----+"
        coluna = "|"

        ex:
        def ExibeJogo():
            print "\n"
            print "\n  +-------+-------+-------+"
            for i in range(3):
                for j in range(3):
                    print "  |  ",Velha[i][j],
                print "  |  ",
                print "\n  +-------+-------+-------+"
            print "\n"
    Para escolher lugar:
        +-------+-------+-------+
        |   0   |   1   |   2   |
        +-------+-------+-------+
        |   3   |   4   |   5   |
        +-------+-------+-------+
        |   6   |   7   |   8   |
        +-------+-------+-------+
        posicao = input("Escolha uma posição de 0 a 8: ")
        escolheu posição 5:
        +-------+-------+-------+
        |       |       |       |
        +-------+-------+-------+
        |       |       |   X   |
        +-------+-------+-------+
        |       |       |       |
        +-------+-------+-------+
exemplo de lógicas:
Velha = [[ " ", " "," "],[ " ", " "," "],[ " ", " "," "]]

def ExibeJogo():
    print "\n"
    print "\n  +-------+-------+-------+"
    for i in range(3):
        for j in range(3):
            print "  |  ",Velha[i][j],
        print "  |  ",
        print "\n  +-------+-------+-------+"
    print "\n"

print Velha
ExibeJogo()
sair = False
    while (sair == False):
        pos = input("Digite a posição da sua jogada (inválido para sair): ")
            if pos >=0 and pos <=8:
                x = int(pos/3)
                y = pos%3
                Velha[x][y] = "X"
                ExibeJogo()
            else:
                sair = True
print ("Fim do Programa")


pra trocar a vez, pode ser:
sair = False
    while (sair == False):
        print "Agora é a vez de ",Quem #onde Quem pode ter valor "X" ou "O"
        pos = input("Digite a posição da sua jogada (inválido para sair): ")
            if pos >=0 and pos <=8:
                x = int(pos/3)
                y = pos%3
                Velha[x][y] = Quem 
                ExibeJogo()
                if(Quem=="X"):
                    Quem = "O"
                else:
                    Quem = "X"
            else:
                sair = True
print ("Fim do Programa")


Implementar inteligência artificial para:
    Verificar se o humano tem chance de vencer na próxima rodada
    Se o meio está vazio
    Se o canto está vazio
    Se o espaço está ocupado
'''
Velha = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#Função para exibir jogo
def ExibeJogo():
    print "\n"
    print "\n  +-------+-------+-------+"
    for i in range(3):
        for j in range(3):
            print "  |  ",Velha[i][j],
        print "  |  ",
        print "\n  +-------+-------+-------+"
    print "\n"
#Função para definir se alguém venceu.
#True se alguém ganhou, False se não acabou o jogo
#O jogador que venceu dá pra buscar pela variável XJogando
def AlguemVenceu():
    #Verificação por linha
    for i in range(3):
        if (Velha[i][0] == Velha[i][1] and Velha[i][1] == Velha[i][2] and Velha[i][0]!=" "):
            return True
    #Verificação por Coluna
    for j in range(3):
        if (Velha[0][j] == Velha[1][j] and Velha[1][j] == Velha[2][j] and Velha[0][j]!=" "):
            return True
    #Verificação por Diagonal
    if (Velha[0][0] == Velha[1][1] and Velha[1][1] == Velha[2][2] and Velha[0][0]!=" "):
        return True
    elif (Velha[0][2] == Velha[1][1] and Velha[1][1] == Velha[2][0] and Velha[0][2]!=" "):
        return True
    return False
#Função para definir se acabaram os movimentos ("Deu velha")
#Só faz sentido ser chamada se AlguemVenceu() der False
def DeuVelha():
    for i in range(3):
        for j in range(3):
            if(Velha[i][j]==" "):
                return False
    return True
#Função para traduzir o número da posição informado (0 a 8),
#retornando as coordenadas de linha e coluna no jogo
def TraduzNumeroParaLinhaColunaVelha(numero):
    linha = numero/3
    coluna = numero%3
    return linha,coluna
#Função para retornar se uma função está ocupada ou não.
def PosicaoEstaOcupada(numero):
    linha,coluna = TraduzNumeroParaLinhaColunaVelha(numero)
    if(Velha[linha][coluna]==" "):
        return False
    else:
        return True
#Aplicação principal
print "Jogo da Velha: Versão Jogador vs Jogador"
print "Quem começa o jogo é sempre o jogador X"
XJogando = True

ExibeJogo()
acabouJogo = False
while(acabouJogo==False):
    if(XJogando == True):
        print "Vez: Jogador \"X\"."
    else:
        print "Vez: Jogador \"O\"."
    posicaoescolhida = input("Escolha uma posição de 0 a 8, representando cada espaço vazio do jogo: ")
    if(posicaoescolhida<0 or posicaoescolhida>8):
        print "Posição inválida. Deve ser um número de 0 a 8."
    elif(PosicaoEstaOcupada(posicaoescolhida)):
        print "Posição ocupada."
    else:
        i,j = TraduzNumeroParaLinhaColunaVelha(posicaoescolhida)
        if(XJogando == True):
            Velha[i][j]="X"
        else:
            Velha[i][j]="O"
        ExibeJogo()
        if(AlguemVenceu()==True):
            acabouJogo=True
            if(XJogando==True):
                print "Jogador \"X\" venceu."
            else:
                print "Jogador \"O\" venceu."
        else:
            if(DeuVelha()):
                acabouJogo=True
                print "Velha. Não há mais movimentos possíveis."
            else:
                if(XJogando==True):
                    XJogando=False
                else:
                    XJogando=True
