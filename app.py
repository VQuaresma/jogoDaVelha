import os 
from time import sleep
import random

ganhador = ''
vitoria=False
jogadas=0
maxJogadas=9
jogador=0
marcador=''
jogo =[ 
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
posx=0
posy=0
quest =''
jogarnovamente=True
vitoriaX =0
vitoriaO =0
def tela():
    
    os.system("cls")
    print("JOGO DA VELHA\n")
    print(f"O jogador X ganhou {vitoriaX} vezes")
    print(f"O jogador O ganhou {vitoriaO} vezes\n")
    print('   0    1    2 ')
    print('0    '+jogo[0][0] + ' | ' + jogo[0][1] + ' | ' + jogo[0][2])
    print('    ---|---|---')
    print('1    '+jogo[1][0] + ' | ' + jogo[1][1] + ' | ' + jogo[1][2])
    print('    ---|---|---')
    print('2    '+jogo[2][0] + ' | ' + jogo[2][1] + ' | ' + jogo[2][2])
    print(f"\nNumero de jogadas: {jogadas}")

def marcar():
    while True:
        posx = int(input("Qual linha você quer marcar? "))
        posy = int(input("Qual coluna você quer marcar? "))
        if jogo[posx][posy] == ' ':
            jogo[posx][posy] = 'X'
            break
        else:
            print("Posição indisponivel! Tente novamente")
        

def cpu():
    while True:
        Xcpu = random.randint(0, 2)
        Ycpu = random.randint(0, 2)
        if jogo[Xcpu][Ycpu]==' ':
            jogo[Xcpu][Ycpu]='O'
            break
        
def verificarVitoria():
    global vitoria
    global ganhador
    global vitoriaX
    global vitoriaO
    # Verificar linhas
    for i in range(3):
        if jogo[i][0] == jogo[i][1] == jogo[i][2]  != ' ':
            vitoria = True
            ganhador = f"Jogador {jogo[i][0]}"
            adicionarVitoria()    
            
    # Verificar colunas
    for i in range(3):
        if jogo[0][i] == jogo[1][i] == jogo[2][i] != ' ':
            vitoria = True
            ganhador = f"Jogador {jogo[0][i]}"
            adicionarVitoria()
    
    # Verificar diagonais
    if jogo[0][0] == jogo[1][1] == jogo[2][2] != ' ':
        vitoria = True
        ganhador = f"Jogador {jogo[0][0]}"
        adicionarVitoria()
    
    if jogo[2][0] == jogo[1][1] == jogo[0][2] != ' ':
        vitoria = True
        ganhador = f"Jogador {jogo[2][0]}"
        adicionarVitoria()

def adicionarVitoria():
    global vitoriaX
    global vitoriaO
    if ganhador == "Jogador X":
            vitoriaX+=1
    elif ganhador == "Jogador O":
            vitoriaO+=1

def telafinal():
    global jogo
    global vitoria
    global jogarnovamente
    global jogadas
    print(f"O ganhador foi o {ganhador} com {jogadas} jogadas!  ")
    
    quest = input("Aperte qualquer tecla para jogar novamente ou aperte ENTER para sair do progama ")
    if quest == '':
        jogarnovamente=False
    else:
        jogadas = 0
        jogo =[ 
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
        ]
        vitoria=False




while True:
    
    while True:
        tela()
        
        marcar()
        jogadas+=1
        tela()
        verificarVitoria()
        if vitoria == True:
            break
        cpu()
        tela()
        verificarVitoria()
        if vitoria == True:
            break    
    telafinal()
    if jogarnovamente==False:
        break
print('progama finalizado!')


