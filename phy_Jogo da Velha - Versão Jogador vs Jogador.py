# -*- coding: cp1252 -*-
'''
Jogo da Velha
1� vers�o: duas pessoas, uma contra a outra
2� vers�o: uma pessoa contra a m�quina
            pergunta se jogador quer jogar com X ou O,
            se joga primeiro ou n�o

Valida se a posi��o escolhida est� ocupada ou n�o
Quando um dos lados ganhar, o programa deve avisar quem foi

Validar se alguma linha, coluna ou diagonal est� com o mesmo valor

Forma de fazer:
    Tabuleiro: vari�vel "Velha" - iniciar vazio
        Velha = [[ " ", " "," "],[ " ", " "," "],[ " ", " "," "]]
    Para desenhar quadro, fun��o ExibeJogo
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
        posicao = input("Escolha uma posi��o de 0 a 8: ")
        escolheu posi��o 5:
        +-------+-------+-------+
        |       |       |       |
        +-------+-------+-------+
        |       |       |   X   |
        +-------+-------+-------+
        |       |       |       |
        +-------+-------+-------+
exemplo de l�gicas:
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
        pos = input("Digite a posi��o da sua jogada (inv�lido para sair): ")
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
        print "Agora � a vez de ",Quem #onde Quem pode ter valor "X" ou "O"
        pos = input("Digite a posi��o da sua jogada (inv�lido para sair): ")
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


Implementar intelig�ncia artificial para:
    Verificar se o humano tem chance de vencer na pr�xima rodada
    Se o meio est� vazio
    Se o canto est� vazio
    Se o espa�o est� ocupado
'''
Velha = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#Fun��o para exibir jogo
def ExibeJogo():
    print "\n"
    print "\n  +-------+-------+-------+"
    for i in range(3):
        for j in range(3):
            print "  |  ",Velha[i][j],
        print "  |  ",
        print "\n  +-------+-------+-------+"
    print "\n"
#Fun��o para definir se algu�m venceu.
#True se algu�m ganhou, False se n�o acabou o jogo
#O jogador que venceu d� pra buscar pela vari�vel XJogando
def AlguemVenceu():
    #Verifica��o por linha
    for i in range(3):
        if (Velha[i][0] == Velha[i][1] and Velha[i][1] == Velha[i][2] and Velha[i][0]!=" "):
            return True
    #Verifica��o por Coluna
    for j in range(3):
        if (Velha[0][j] == Velha[1][j] and Velha[1][j] == Velha[2][j] and Velha[0][j]!=" "):
            return True
    #Verifica��o por Diagonal
    if (Velha[0][0] == Velha[1][1] and Velha[1][1] == Velha[2][2] and Velha[0][0]!=" "):
        return True
    elif (Velha[0][2] == Velha[1][1] and Velha[1][1] == Velha[2][0] and Velha[0][2]!=" "):
        return True
    return False
#Fun��o para definir se acabaram os movimentos ("Deu velha")
#S� faz sentido ser chamada se AlguemVenceu() der False
def DeuVelha():
    for i in range(3):
        for j in range(3):
            if(Velha[i][j]==" "):
                return False
    return True
#Fun��o para traduzir o n�mero da posi��o informado (0 a 8),
#retornando as coordenadas de linha e coluna no jogo
def TraduzNumeroParaLinhaColunaVelha(numero):
    linha = numero/3
    coluna = numero%3
    return linha,coluna
#Fun��o para retornar se uma fun��o est� ocupada ou n�o.
def PosicaoEstaOcupada(numero):
    linha,coluna = TraduzNumeroParaLinhaColunaVelha(numero)
    if(Velha[linha][coluna]==" "):
        return False
    else:
        return True
#Aplica��o principal
print "Jogo da Velha: Vers�o Jogador vs Jogador"
print "Quem come�a o jogo � sempre o jogador X"
XJogando = True

ExibeJogo()
acabouJogo = False
while(acabouJogo==False):
    if(XJogando == True):
        print "Vez: Jogador \"X\"."
    else:
        print "Vez: Jogador \"O\"."
    posicaoescolhida = input("Escolha uma posi��o de 0 a 8, representando cada espa�o vazio do jogo: ")
    if(posicaoescolhida<0 or posicaoescolhida>8):
        print "Posi��o inv�lida. Deve ser um n�mero de 0 a 8."
    elif(PosicaoEstaOcupada(posicaoescolhida)):
        print "Posi��o ocupada."
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
                print "Velha. N�o h� mais movimentos poss�veis."
            else:
                if(XJogando==True):
                    XJogando=False
                else:
                    XJogando=True
