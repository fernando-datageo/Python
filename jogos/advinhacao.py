'''
    Consist em um jogo de advinhar um numero aleatório de 1 a 100
    A pontuação esta relacionada a quantidade e distanciamento dos
    chutes em relação ao numero secreto.
'''

import random

def jogar():

    print("\n----------------------------------")
    print("Bem vindo ao jogo de adviuinhação!")
    print("----------------------------------\n")

    # Base inicial para o random "random"
    random.seed(random.random())

    numero_secreto = random.randrange(1, 101) # nº aleatorio inteiro entre 1 e 100

    total_tentativas = 0
    rodada = 1
    pontos = 1000 # Pontos iniciais

    print("Qual o nível de dificuldade você de deseja?\n")
    print("(1) Fácil (2) Médio (3) Difícil: ")

    nivel = int(input("Defina o nível: "))

    # Condições de tentativas segundo nível de dificuldade
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    # Laço de msg interativas ao jogador
    for rodada in range(1, total_tentativas +1):

        print(f"Tentativa {rodada} de {total_tentativas}\n")
        chute = int(input("Digite o seu número entre 1 e 100: "))
        print("Você digitou ", chute, "\n")

        # Condição para entrada de chutes verdadeiros
        if(chute < 1 or chute > 100):
            print("Você deve digitar um nº entre 1 e 100!\n")
            continue

        # Condiçoes básicas para determinar a equivalência do chute
        acertou = chute == numero_secreto
        mais = chute > numero_secreto
        menos = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos} pontos!\n")
            break
        else:
            if(mais):
                print("Você errou, para MAIS...\n")
            elif(menos):
                print("Você errou, para MENOS...\n")

            # Condição de cálculo da pontuação final
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo.")

# Se o arquivo aberto for o arquivo principal rodar a função jogar()
if(__name__ == "__main__"):
    jogar()