import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2020100123" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Isabella Gabrielle da Silva Pinheiro" 

def limpaTela():
    if name == 'nt': 
	    system('cls') 
    else: 
	    system('clear') 

def jogadaJogador(tab, escolhasimbolo):
    """
    Pergunta ao jogador onde ele quer jogar, e também verifica algumas posiçõs inválidas (pois alguém já jogou nela).
    """
    i = int((input("Onde deseja jogar? (1-9) ")))
    if (i < 1) or (i > 9):
        print("Posição inválida. Escolha outra!")
        return jogadaJogador(tab,escolhasimbolo)
    elif (tab[i] != " "):
        print("Essa posição já foi escolhida. Escolha outra!")
        return jogadaJogador(tab,escolhasimbolo)
    else:
        return i

def verificaçãodedefesa(tab,simbolocomp,escolhasimbolo):
    """
    Isso faz parte da estratégia do computador. Essa função verifica se há possibilidade de se defender do jogador, e retorna a defesa. 
    Se não tiver algo pra se defender, retorna None.
    """
    #linha 1-2-3
    if (tab[1]==escolhasimbolo and tab[2]==escolhasimbolo and tab[3]== " "):
        return 3
    elif (tab[1]==escolhasimbolo and tab[3]==escolhasimbolo and tab[2]== " "):
        return 2
    elif (tab[2]==escolhasimbolo and tab[3]==escolhasimbolo and tab[1] == " "):
        return 1
    #linha 4-5-6
    elif (tab[4]==escolhasimbolo and tab[5]==escolhasimbolo and tab[6]== " "):
        return 6
    elif (tab[4]==escolhasimbolo and tab[6]==escolhasimbolo and tab[5]== " "):
        return 5
    elif (tab[5]==escolhasimbolo and tab[6]==escolhasimbolo and tab[4] == " "):
        return 4
    #linha 7-8-9
    elif (tab[7]==escolhasimbolo and tab[8]==escolhasimbolo and tab[9]== " "):
        return 9
    elif (tab[7]==escolhasimbolo and tab[9]==escolhasimbolo and tab[8]== " "):
        return 8
    elif (tab[8]==escolhasimbolo and tab[9]==escolhasimbolo and tab[7] == " "):
        return 7
    #linha 3-6-9
    elif (tab[3]==escolhasimbolo and tab[6]==escolhasimbolo and tab[9]== " "):
        return 9
    elif (tab[3]==escolhasimbolo and tab[9]==escolhasimbolo and tab[6]== " "):
        return 6
    elif (tab[9]==escolhasimbolo and tab[6]==escolhasimbolo and tab[3] == " "):
        return 3
    #linha 2-5-8
    elif (tab[2]==escolhasimbolo and tab[5]==escolhasimbolo and tab[8]== " "):
        return 8
    elif (tab[2]==escolhasimbolo and tab[8]==escolhasimbolo and tab[5]== " "):
        return 5
    elif (tab[8]==escolhasimbolo and tab[5]==escolhasimbolo and tab[2] == " "):
        return 2
    #linha 1-4-7
    elif (tab[1]==escolhasimbolo and tab[4]==escolhasimbolo and tab[7]== " "):
        return 7
    elif (tab[1]==escolhasimbolo and tab[7]==escolhasimbolo and tab[4]== " "):
        return 4
    elif (tab[4]==escolhasimbolo and tab[7]==escolhasimbolo and tab[1] == " "):
        return 1
    #linha 1-5-9
    elif (tab[1]==escolhasimbolo and tab[5]==escolhasimbolo and tab[9]== " "):
        return 9
    elif (tab[1]==escolhasimbolo and tab[9]==escolhasimbolo and tab[5]== " "):
        return 5
    elif (tab[5]==escolhasimbolo and tab[9]==escolhasimbolo and tab[1] == " "):
        return 1
    #linha 3-5-7
    elif (tab[3]==escolhasimbolo and tab[5]==escolhasimbolo and tab[7]== " "):
        return 7
    elif (tab[3]==escolhasimbolo and tab[7]==escolhasimbolo and tab[5]== " "):
        return 5
    elif (tab[5]==escolhasimbolo and tab[7]==escolhasimbolo and tab[3] == " "):
        return 3
    else: #Se o pc não precisa se defender, ele vai atacar nas quinas.
        if tab[1] == " ":
            return 1
        if tab[3] == " ":
            return 3
        if tab[7] == " ":
            return 7
        if tab[9] == " ":
            return 9


def jogadaComputador(tab, simbolocomp,i,escolhasimbolo,hm):
    """
    Recebe o tabuleiro, simbolo (X ou O) do computador, i seria a rodada, escolhasimbolo seria a escolha do jogador.
    Essa função foi construída em cima daquela estratégia das quinas. 
    Na rodada 1, o computador tenta marcar nas quinas.
    Na rodada 2, o computador verifica se precisa se defender, e se não, tenta marcar nas quinas de novo.
    Na rodada 3, mesma coisa.
    Na 4 em diante ele tenta defender, caso não tenha o que ser defendido, tenta ganhar.
    O hm é uma tática que estou testando de jogar no meio pra quebrar alguma estratégia do jogador caso o jogador comece jogando. 
    """
    print("Vez do computador.")    
    l = [l for l in range(1, len(tab)) if tab[l] == " "]
    print(l)
    #TÁTICA PARA ESCOLHER CASAS NAS QUINAS
    if i == 1:
        if hm == 1:
            if tab[5] == " ":
                return 5
            else:
                if tab[1] == escolhasimbolo:
                    escolha = random.choice('379')
                    escolhaint = int(escolha)
                    return escolhaint
                elif tab[3] == escolhasimbolo:
                    escolha = random.choice('179')
                    escolhaint = int(escolha)
                    return escolhaint
                elif tab[7] == escolhasimbolo:
                    escolha = random.choice('319')
                    escolhaint = int(escolha)
                    return escolhaint
                elif tab[9] == escolhasimbolo:
                    escolha = random.choice('371')
                    escolhaint = int(escolha)
                    return escolhaint
                elif (tab[1] == " ") and (tab[3] == " ") and (tab[7] == " ") and (tab[9] == " "):
                    escolha = random.choice('1379')
                    escolhaint = int(escolha)
                    return escolhaint
        else:
            if tab[1] == escolhasimbolo:
                escolha = random.choice('379')
                escolhaint = int(escolha)
                return escolhaint
            elif tab[3] == escolhasimbolo:
                escolha = random.choice('179')
                escolhaint = int(escolha)
                return escolhaint
            elif tab[7] == escolhasimbolo:
                escolha = random.choice('319')
                escolhaint = int(escolha)
                return escolhaint
            elif tab[9] == escolhasimbolo:
                escolha = random.choice('371')
                escolhaint = int(escolha)
                return escolhaint
            elif (tab[1] == " ") and (tab[3] == " ") and (tab[7] == " ") and (tab[9] == " "):
                escolha = random.choice('1379')
                escolhaint = int(escolha)
                return escolhaint
    if i==2:
        #verificação de defesa, usando a estratégia da quina
        #essa estratégia da linha 2 eu me baseei no tic tac toe do google, ele sempre joga nessa posição quando o jogador tá nessa indicada.
        if (tab[1] == escolhasimbolo and tab[9] == escolhasimbolo) or (tab[3] == escolhasimbolo and tab[7] == escolhasimbolo):
            return 8
        else:
            return verificaçãodedefesa(tab,simbolocomp,escolhasimbolo)
    
    if i==3:
        #verificação de defesa, usando a estratégia da quina
        return verificaçãodedefesa(tab,simbolocomp,escolhasimbolo)
                
            
    #ROAD TO WIN = MODO ATAQUE
    #linha 1-2-3
    if (tab[1]==simbolocomp and tab[2]==simbolocomp and tab[3]== " "):
        return 3
    elif (tab[1]==simbolocomp and tab[3]==simbolocomp and tab[2]== " "):
        return 2
    elif (tab[3]==simbolocomp and tab[2]==simbolocomp and tab[1] == " "):
        return 1
    #linha 4-5-6
    elif (tab[4]==simbolocomp and tab[5]==simbolocomp and tab[6]== " "):
        return 6
    elif (tab[4]==simbolocomp and tab[6]==simbolocomp and tab[5]== " "):
        return 5
    elif (tab[5]==simbolocomp and tab[6]==simbolocomp and tab[4] == " "):
        return 4
    #linha 7-8-9
    elif (tab[7]==simbolocomp and tab[8]==simbolocomp and tab[9]== " "):
        return 9
    elif (tab[7]==simbolocomp and tab[9]==simbolocomp and tab[8]== " "):
        return 8
    elif (tab[8]==simbolocomp and tab[9]==simbolocomp and tab[7] == " "):
        return 7
    #linha 3-6-9
    elif (tab[3]==simbolocomp and tab[6]==simbolocomp and tab[9]== " "):
        return 9
    elif (tab[3]==simbolocomp and tab[9]==simbolocomp and tab[6]== " "):
        return 6
    elif (tab[9]==simbolocomp and tab[6]==simbolocomp and tab[3] == " "):
        return 3
    #linha 2-5-8
    elif (tab[2]==simbolocomp and tab[5]==simbolocomp and tab[8]== " "):
        return 8
    elif (tab[2]==simbolocomp and tab[8]==simbolocomp and tab[5]== " "):
        return 5
    elif (tab[8]==simbolocomp and tab[5]==simbolocomp and tab[2] == " "):
        return 2
    #linha 1-4-7
    elif (tab[1]==simbolocomp and tab[4]==simbolocomp and tab[7]== " "):
        return 7
    elif (tab[1]==simbolocomp and tab[7]==simbolocomp and tab[4]== " "):
        return 4
    elif (tab[4]==simbolocomp and tab[7]==simbolocomp and tab[1] == " "):
        return 1
    #linha 1-5-9
    elif (tab[1]==simbolocomp and tab[5]==simbolocomp and tab[9]== " "):
        return 9
    elif (tab[1]==simbolocomp and tab[9]==simbolocomp and tab[5]== " "):
        return 5
    elif (tab[5]==simbolocomp and tab[9]==simbolocomp and tab[1] == " "):
        return 1
    #linha 3-5-7
    elif (tab[3]==simbolocomp and tab[5]==simbolocomp and tab[7]== " "):
        return 7
    elif (tab[3]==simbolocomp and tab[7]==simbolocomp and tab[5]== " "):
        return 5
    elif (tab[5]==simbolocomp and tab[7]==simbolocomp and tab[3] == " "):
        return 3
    #NÃO VENCI? VOU ME DEFENDER   
    #linha 1-2-3
    elif (tab[1]==escolhasimbolo and tab[2]==escolhasimbolo and tab[3]== " "):
        return 3
    elif (tab[1]==escolhasimbolo and tab[3]==escolhasimbolo and tab[2]== " "):
        return 2
    elif (tab[2]==escolhasimbolo and tab[3]==escolhasimbolo and tab[1] == " "):
        return 1
    #linha 4-5-6
    elif (tab[4]==escolhasimbolo and tab[5]==escolhasimbolo and tab[6]== " "):
        return 6
    elif (tab[4]==escolhasimbolo and tab[6]==escolhasimbolo and tab[5]== " "):
        return 5
    elif (tab[5]==escolhasimbolo and tab[6]==escolhasimbolo and tab[4] == " "):
        return 4
    #linha 7-8-9
    elif (tab[7]==escolhasimbolo and tab[8]==escolhasimbolo and tab[9]== " "):
        return 9
    elif (tab[7]==escolhasimbolo and tab[9]==escolhasimbolo and tab[8]== " "):
        return 8
    elif (tab[8]==escolhasimbolo and tab[9]==escolhasimbolo and tab[7] == " "):
        return 7
    #linha 3-6-9
    elif (tab[3]==escolhasimbolo and tab[6]==escolhasimbolo and tab[9]== " "):
        return 9
    elif (tab[3]==escolhasimbolo and tab[9]==escolhasimbolo and tab[6]== " "):
        return 6
    elif (tab[9]==escolhasimbolo and tab[6]==escolhasimbolo and tab[3] == " "):
        return 3
    #linha 2-5-8
    elif (tab[2]==escolhasimbolo and tab[5]==escolhasimbolo and tab[8]== " "):
        return 8
    elif (tab[2]==escolhasimbolo and tab[8]==escolhasimbolo and tab[5]== " "):
        return 5
    elif (tab[8]==escolhasimbolo and tab[5]==escolhasimbolo and tab[2] == " "):
        return 2
    #linha 1-4-7
    elif (tab[1]==escolhasimbolo and tab[4]==escolhasimbolo and tab[7]== " "):
        return 7 
    elif (tab[1]==escolhasimbolo and tab[7]==escolhasimbolo and tab[4]== " "):
        return 4
    elif (tab[4]==escolhasimbolo and tab[7]==escolhasimbolo and tab[1] == " "):
        return 1
    #linha 1-5-9
    elif (tab[1]==escolhasimbolo and tab[5]==escolhasimbolo and tab[9]== " "):
        return 9
    elif (tab[1]==escolhasimbolo and tab[9]==escolhasimbolo and tab[5]== " "):
        return 5
    elif (tab[5]==escolhasimbolo and tab[9]==escolhasimbolo and tab[1] == " "):
        return 1
    #linha 3-5-7
    elif (tab[3]==escolhasimbolo and tab[5]==escolhasimbolo and tab[7]== " "):
        return 7
    elif (tab[3]==escolhasimbolo and tab[7]==escolhasimbolo and tab[5]== " "):
        return 5
    elif (tab[5]==escolhasimbolo and tab[7]==escolhasimbolo and tab[3] == " "):
        return 3
    # NÃO TEM DEFESA NEM VITÓRIA? VOU DE FORMA RANDOMICA
    else:
        escolha = random.choice(l)
        return escolha 


def escolhaJogador():
    """
    Função que pergunta ao jogador o que ele deseja ser.
    """
    simboloJogador = input("Você quer ser 'X' ou 'O'? ")
    simboloComputador = ''
    if simboloJogador == 'O' or simboloJogador == 'o':
        return "O"
    elif simboloJogador == 'X' or simboloJogador == 'x':
        return "X"
    elif simboloJogador != 'X' or simboloJogador != 'O' or simboloJogador != 'x' or simboloJogador != 'O':
        print("Simbolo inválido! Escolha X ou O.")
        return escolhaJogador()

def quemcomeçara():
    """
    Função que define quem começa, pois sorteia 1 ou 2
    Se 2, o jogador começa. Se 1, o computador começa.
    """
    quemcomeça = random.randint(1,2)    
    if quemcomeça == 2:
        print("Você começa.")
        return quemcomeça        
    elif quemcomeça == 1:
        print("O computador começa.")
        return quemcomeça

def imprimetabuleiro(tab):
    """
    Função que imprime o tabuleiro.
    """
    
    print(f" {tab[7]} | {tab[8]} | {tab[9]}")
    print("---+---+---")
    print(f" {tab[4]} | {tab[5]} | {tab[6]}")
    print("---+---+---")
    print(f" {tab[1]} | {tab[2]} | {tab[3]}")

   
def seXvenceu(tab):
    """
    Verifica se x venceu em algum momento do tabuleiro.
    """
    # |
    if tab[1] == 'X' and tab[4] == 'X' and tab[7] == 'X':
        return True
    if tab[2] == 'X' and tab[5] == 'X' and tab[8] == 'X':
        return True
    if tab[3] == 'X' and tab[6] == 'X' and tab[9] == 'X':
        return True
    # /\
    if tab[1] == 'X' and tab[5] == 'X' and tab[9] == 'X':
        return True
    if tab[3] == 'X' and tab[5] == 'X' and tab[7] == 'X':
        return True    
    # -
    if tab[7] == 'X' and tab[8] == 'X' and tab[9] == 'X':
        return True
    if tab[4] == 'X' and tab[5] == 'X' and tab[6] == 'X':
        return True
    if tab[1] == 'X' and tab[2] == 'X' and tab[3] == 'X':
        return True

def seOvenceu(tab):
    """
    Verifica se O venceu em algum momento do tabuleiro.
    """
    # |
    if tab[1] == 'O' and tab[4] == 'O' and tab[7] == 'O':
        return True
    if tab[2] == 'O' and tab[5] == 'O' and tab[8] == 'O':
        return True
    if tab[3] == 'O' and tab[6] == 'O' and tab[9] == 'O':
        return True
    # /\
    if tab[1] == 'O' and tab[5] == 'O' and tab[9] == 'O':
        return True
    if tab[3] == 'O' and tab[5] == 'O' and tab[7] == 'O':
        return True    
    # -
    if tab[7] == 'O' and tab[8] == 'O' and tab[9] == 'O':
        return True
    if tab[4] == 'O' and tab[5] == 'O' and tab[6] == 'O':
        return True
    if tab[1] == 'O' and tab[2] == 'O' and tab[3] == 'O':
        return True


        
def jogadas1(tab,escolhasimbolo,simbolocomp,i=1):
    """
    Caso o jogador comece, vamos seguir essa linha de movimentação.
    Coloquei verificação dos livres, se x vence, se o vence, e depois verifico empate. 
    Se não rolou essas três condições, então manda rolar de novo a movimentação, acrescentando i = i + 1 
    hm é uma tática que estou usando pro computador escolher a posição do meio pra quebrar algumas táticas que pode vim. 
    """
    hm=1
    tab[jogadaJogador(tab,escolhasimbolo)] = escolhasimbolo
    imprimetabuleiro(tab)
    l = [l for l in range(1, len(tab)) if tab[l] == " "]   
    seXvenceu(tab)
    seOvenceu(tab)
    if seOvenceu(tab) == True and simbolocomp == 'O':
        print("O computador venceu. ")
        x = input("--> Enter para continuar...")
        exit()
    elif seOvenceu(tab) == True and escolhasimbolo == 'O':
        print("Você ganhou!")
        x = input("--> Enter para continuar...")
        exit()
    elif seXvenceu(tab) == True and simbolocomp == 'X':
        print("O computador venceu. ")
        x = input("--> Enter para continuar...")
        exit()
    elif seXvenceu(tab) == True and escolhasimbolo == 'X':
        print("Você ganhou!")
        x = input("--> Enter para continuar...")
        exit()
    elif l==[]:
        print("Empatou!")
        x = input("--> Enter para continuar...")
        exit()                 
    tab[jogadaComputador(tab,simbolocomp,i,escolhasimbolo,hm)] = simbolocomp
    imprimetabuleiro(tab)
    l = [l for l in range(1, len(tab)) if tab[l] == " "]   
    seXvenceu(tab)
    seOvenceu(tab)
    if seOvenceu(tab) == True and simbolocomp == 'O':
        print("O computador venceu. ")
        x = input("--> Enter para continuar...")
        exit()
    elif seOvenceu(tab) == True and escolhasimbolo == 'O':
        print("Você ganhou!")
        x = input("--> Enter para continuar...")
        exit()
    elif seXvenceu(tab) == True and simbolocomp == 'X':
        print("O computador venceu. ")
        x = input("--> Enter para continuar...")
        exit()
    elif seXvenceu(tab) == True and escolhasimbolo == 'X':
        print("Você ganhou!")
        x = input("--> Enter para continuar...")
        exit()
    elif l==[]:
        print("Empatou!")
        x = input("--> Enter para continuar...")
        exit()    
    else:
        jogadas1(tab,escolhasimbolo,simbolocomp,i=i+1)

        

def jogadas2(tab,escolhasimbolo,simbolocomp,i=1):
    """
    Caso o computador comece, vamos seguir essa linha de movimentação.
    Coloquei verificação dos livres, se x vence, se o vence, e depois verifico empate. 
    Se não rolou essas três condições, então manda rolar de novo a movimentação, acrescentando i = i + 1
    """
    hm = 0
    tab[jogadaComputador(tab,simbolocomp,i,escolhasimbolo,hm)] = simbolocomp    
    imprimetabuleiro(tab)
    l = [l for l in range(1, len(tab)) if tab[l] == " "]
    seXvenceu(tab)
    seOvenceu(tab)
    if seOvenceu(tab) == True and simbolocomp == 'O':
        print("O computador venceu. ")
        x = input("--> Enter para continuar...")
        exit()
    elif seOvenceu(tab) == True and escolhasimbolo == 'O':
        print("Você ganhou!")
        x = input("--> Enter para continuar...")
        exit()
    elif seXvenceu(tab) == True and simbolocomp == 'X':
        print("O computador venceu. ")
        x = input("--> Enter para continuar...")
        exit()
    elif seXvenceu(tab) == True and escolhasimbolo == 'X':
        print("Você ganhou!")
        x = input("--> Enter para continuar...")
        exit()  
    elif l==[]:
        print("Empatou!")
        x = input("--> Enter para continuar...")
        exit()                  
    tab[jogadaJogador(tab,escolhasimbolo)] = escolhasimbolo
    imprimetabuleiro(tab)
    l = [l for l in range(1, len(tab)) if tab[l] == " "]
    seXvenceu(tab)
    seOvenceu(tab)
    if seOvenceu(tab) == True and simbolocomp == 'O':
        print("O computador venceu. ")
        x = input("--> Enter para continuar...")
        exit()
    elif seOvenceu(tab) == True and escolhasimbolo == 'O':
        print("Você ganhou!")
        x = input("--> Enter para continuar...")
        exit()
    elif seXvenceu(tab) == True and simbolocomp == 'X':
        print("O computador venceu. ")
        x = input("--> Enter para continuar...")
        exit()
    elif seXvenceu(tab) == True and escolhasimbolo == 'X':
        print("Você ganhou!")
        x = input("--> Enter para continuar...")
        exit()       
    elif l==[]:
        print("Empatou!")
        x = input("--> Enter para continuar...")
        exit()        
    else:
        jogadas2(tab,escolhasimbolo,simbolocomp,i=i+1)

    
def main():
    """
    Central, aqui invoco as funções.
    """
    limpaTela()
    print(getMatricula())
    print(getNome())
    print("Bem vindo ao clássico Jogo da Velha!")
    tab = [" "]*10
    simbolocomp = 0
    quemcomeça = 0
    escolhasimbolo = escolhaJogador()
    if escolhasimbolo == 'X':
        simbolocomp = 'O' 
    else:
        simbolocomp = 'X'
    quemcomeça = quemcomeçara() #Escolhe 1 ou 2. Se for 1, Jogador começa. Se for 2, Computador começa.
    imprimetabuleiro(tab)
    if quemcomeça == 1:
        jogadas2(tab,escolhasimbolo,simbolocomp)
    else:   
        jogadas1(tab,escolhasimbolo,simbolocomp)
       
main() 

if __name__ == "__main__":
    main()