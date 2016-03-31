#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include <graphics.h>

using namespace std;

char velha[3][3] = 
{
		{' ', ' ', ' '},
		{' ', ' ', ' '},
		{' ', ' ', ' '}
};

// Inicializacao das variaveis!
bool XJogando = true;								//definir quem esta jogando
bool acabouJogo = false;							//verifica se acabou o jogo
int num = 0;										//variavel de controle
int linha = 0;										//representa a coordenada X da velha
int coluna = 0;										//representa a coodenada Y da velha
int posicaoEscolhida = 0;							//verifica a posicao escolhida do usuario
int posicaoEstaOcupada = 0;							//verifica se a posicao esta ocupada

// prototipo da funcao
int ExibeJogo (int i, int j);						//mostrar o jogo da tela
int AlguemVenceu (int i, int j);					//verificar se existe vencedor na rodada
int DeuVelha ();									//verificar se deu velha
void TraduzNumeroParaLinhaColunaVelha(int num);		//traduzir o numero inserido para linha/coluna 
int PosicaoEstaOcupada(int num);					//verificar se uma posicao esta ocupada

int main()
{
	int i, j;
	int posicaoEscolhida, posicaoEstaOcupada;
	bool XJogando = true;
	bool acabouJogo = false;
	
	// Inicializacao as variaveis!!
	i = 0;
	j = 2;
	int * point;
	num = 0;

	std::cout << "Jogo da Velha: Versao Jogador vs Jogador" << std::endl;
	std::cout << "Quem comeca o jogo eh sempre o jogador X"	<< std::endl;
	
	ExibeJogo(i,j);
	
	initwindow(400, 300);
	
	while(acabouJogo==false)
	{
    	if(XJogando == true)
    	{
        	std::cout << "Vez: Jogador X " << std::endl;
   		}
		   else
		   {
        	std::cout << "Vez: Jogador O " << std::endl;
			}
		 	std::cout << "Escolha uma posicao de 0 a 8, representando cada espaco vazio do jogo: " << std::endl;
     		std::cin >> posicaoEscolhida;
    
		if(posicaoEscolhida<0 or posicaoEscolhida>8)
		{
    		std::cout << "Posicao invalida. Deve ser um numero de 0 a 8." << std::endl;
		}
    	else if(PosicaoEstaOcupada(posicaoEscolhida))
		{
        	std::cout << "Posicao ocupada." << std::endl;
    	}
		else
		{
			TraduzNumeroParaLinhaColunaVelha(posicaoEscolhida);	
				
			if(XJogando == true)
            	velha[linha][coluna]='X';
        	else
            	velha[linha][coluna]='O';
        	if(AlguemVenceu(linha, coluna) == true)
			{
            	acabouJogo = true;
            	if(XJogando == true)
            	{
                	std::cout << "Jogador X venceu." << std::endl;
            	}
				else
				{
                	std::cout << "Jogador O venceu." << std::endl;
        		}
			}
			else
			{
            	if(DeuVelha())
            	{
                	acabouJogo=true;
                	std::cout << "Velha. Nao ha mais movimentos possiveis." << std::endl;
            	}
				else
				{
                	if(XJogando==true)
                	{
                    	XJogando=false;
                	}
					else
					{
                   		XJogando=true;
					}    			
				}
			}    
		}
		ExibeJogo(i,j); //exibe o jogo após cada jogada
	}
	while (!kbhit()); //para o jogo nao encerrar após a a execucao do programa
	
	return 0;
}

// funcao para exibir jogo
int ExibeJogo(int i, int j)
{
	for(int l = 0; l < 3; l++)
	{
		for(int c = 0; c < 3; c++)
		{
			std::cout << " | " << velha[l][c] << " | ";	
		}
		
		// quebra a linha
		std::cout << std::endl;
	}
	return velha[i][j];
}

//funcao para verificar se ha vencedor
int AlguemVenceu(int i, int j)
{
    //Verificação por linha
    for(i = 0; i < 3; i++)
	{
        if (velha[i][0] == velha[i][1] && velha[i][1] == velha[i][2] && velha[i][0]!= ' ' )
        {
            return true;
		}
	}
	//Verificacao por Coluna
    for(j = 0; j < 3; j++)
    {
        if (velha[0][j] == velha[1][j] && velha[1][j] == velha[2][j] && velha[0][j]!= ' ' )
        {
            return true;
        }
    //Verificacao por Diagonal
    if (velha[0][0] == velha[1][1] && velha[1][1] == velha[2][2] && velha[0][0]!= ' ' )
    {
        return true;
    }
    else if (velha[0][2] == velha[1][1] && velha[1][1] == velha[2][0] && velha[0][2]!= ' ' )
    {
	    return true;
    }
	return false;
	}	
}

//Verificar se deu velha
int DeuVelha()
{
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            if(velha[i][j] == ' ')
            {
                return false;
            }
    	}
	}
    return true;
}

//funcao para traduzir o numero da posicao informado (0 a 8) retornando as coordenadas de linha e colunas
void TraduzNumeroParaLinhaColunaVelha(int num)
{
    linha = num/3;
    coluna = num%3;
}

//funcao para retornar se uma posicao esta ocupada ou nao
int PosicaoEstaOcupada(int num)
{
    TraduzNumeroParaLinhaColunaVelha(num);
    if(velha[linha][coluna]== ' ')
    {	
        return false;
    }
	else
	{
        return true;
	}
}
