#include <iostream>
#include <istream>
#include<stdio.h>
#include <stdlib.h>
#include <string.h>

// Se vc vai usar a mesma variável em diferentes escopos ( {} é um escopo) ou ela tem que ser global ou tem que 
//  passar por parâmetro. Lembre-se de conversarmos sobre isso
char velha[3][3] = 
{
		{' ', ' ', ' '},
		{' ', ' ', ' '},
		{' ', ' ', ' '}
};


// Inicialize as variáveis!!

int e = 0;
bool XJogando = true;
bool acabouJogo = false;
int i = 0;
int j = 2;
int num = 0;
int linha = 0;
int coluna = 0;
int posicaoEscolhida = 0;
int posicaoEstaOcupada = 0;


// protótipo da função
int ExibeJogo (int i, int j); //mostrar o jogo da tela
int AlguemVenceu (int i, int j); //verificar se existe vencedor na rodada
int DeuVelha (int i, int j); //verificar se deu velha
int TraduzNumeroParaLinhaColunaVelha(int num); //traduzir o numero inserido para linha/coluna 
int PosicaoEstaOcupada(int num); //verificar se uma posicao esta ocupada

int main()
{
	int i, j, e;
	int posicaoEscolhida, posicaoEstaOcupada;
	bool XJogando = true;
	bool acabouJogo = false;
	
	// Inicialize as variáveis!!
	i = 0;
	j = 2;
	num = 0;
	
	
	std::cout << "Jogo da Velha: Versao Jogador vs Jogador" << std::endl;
	std::cout << "Quem começa o jogo eh sempre o jogador X"	<< std::endl;

	int ExibeJogo(int i, int j);
	
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
		 	std::cout << "Escolha uma posicao de 0 a 8, representando cada espaço vazio do jogo: " << std::endl;
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
        	i,j = TraduzNumeroParaLinhaColunaVelha(posicaoEscolhida);
        	if(XJogando == true)
            	velha[i][j]='X';
        	else
            	velha[i][j]='O';
        	int ExibeJogo(int i, int j);
        	if(AlguemVenceu(i, j) == true)
			{
            	int acabouJogo = true;
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
            	if(DeuVelha(i, j))
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
	}
	
	e = ExibeJogo(i,j);
	//printf(e); procure ler sobre a função print, ela é um tanto mais complicada de se usar do que no python
	
	// Uma vez que vc incluiu o iostream, use o cout, é mais fácil
	//std::cout << "e = " << e << std::endl;
}

// funcao para exibir jogo
int ExibeJogo(int i, int j)
{
	for(int l = 0; l < 3; l++)
	{
		for(int c = 0; c < 3; c++)
		{
			//printf("%d ", velha[i][j]);
			std::cout << " | " << velha[l][c] << " | ";
			
		}
		
		// quebra a linha
		std::cout << std::endl;

		//return velha[i][j]; Com o return aqui ele só executaria o loop uma vez.
	}
	// o return deve estar aqui fora do primeiro for, se a intenção era imprimir apenas a primeira linha então ele sequer era necessário.
	return velha[i][j];
}

//funcao para verificar se há vencedor
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
	//Verificação por Coluna
    for(j = 0; j < 3; j++)
    {
        if (velha[0][j] == velha[1][j] && velha[1][j] == velha[2][j] && velha[0][j]!= ' ' )
        {
            return true;
        }
    //Verificação por Diagonal
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

//verificar se deu velha
int DeuVelha(int i, int j)
{
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 3; j++)
        {
            if(velha[i][j] == 0)
            {
                return false;
            }
    	}
	}
    return true;
}

//funcao para traduzir o numero da posicao informado (1 a 9) retornando as coordenadas de linha e colunas
int TraduzNumeroParaLinhaColunaVelha(int num)
{
    linha = num/3;
    coluna = num%3;
    return linha,coluna;
}

//funcao para retornar se uma posicao está ocupada ou nao
int PosicaoEstaOcupada(int num)
{
    linha,coluna = TraduzNumeroParaLinhaColunaVelha(num);
    if(velha[linha][coluna]== ' ')
    {	
        return false;
    }
	else
	{
        return true;
	}
}
