'''
    Tradicional jogo da forca, as palavras secretas são importadas
    de um arquivo externo de texto e sorteadas aleatoriamente.
'''

import random

def jogar():

    # Funções de funcionamento do jogo
    msg_abertura()
    palavra_secreta = carrega_palavra_secreta("palavras.txt")
    letras_acertadas = icializa_palavra(palavra_secreta)
    tamanho = int(len(palavra_secreta))

    print(f'Palavra secreta ({tamanho} letras)\n')
    print(letras_acertadas)

    chance = 7
    print(f"\nVocê tem {chance} chances para advinhar!")
    erros = 0

    # Laço principal do jogo
    while (True):

        chute = pede_chute()

        # Laço que determina a relação do chute com a palavra secreta
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

            desenha_forca(erros)

            print(f"ERROU! ({erros} de {chance})")

       # Determina o fim das chances
        if(erros == chance):
            break

    # Condições para mensagns finais
    if("_" not in letras_acertadas):
        msg_vitoria()
    else:
        msg_derrota(palavra_secreta)

def msg_abertura():
    print("\n---------------------------------")
    print("-- Bem vindo ao jogo da Forca! --")
    print("---------------------------------\n")

# Carrega um arquivo externo no modo leitura desde a primeira linha com palavras secretas par o jogo
def carrega_palavra_secreta(nome_arquivo = "palavras.txt", primeira_linha_valida = 0):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip() # Retira os espaços antees e depois de cada palavra
        palavras.append(linha) # Adiciona cada palavra a lista palavras

    arquivo.close()

    # Cria uma variavel que recebe um numero aleatório equivalente a quantidade de posições da list palavras
    numero = random.randrange(primeira_linha_valida, len(palavras))
    # Deixa a palavra secreta em maiúsculo
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

# Preenche com _ equivalente ao tamanho da palavra secreta
def icializa_palavra(palavra):
    return ["_" for letra in palavra]

# Pede o chute, retira espaços antes e depois da palavra e coloca tudo em miúsculo
def pede_chute():
    return input("\nQual letra? \n").strip().upper()

# Percorre a palavra secreta, substituindo o chute na posição certa em caso de acerto
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

# Mensagens finais
def msg_vitoria():
    print("Parabéns, você ganhou!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def msg_derrota(palavra_secreta):
    print("\nPuxa, você foi enforcado!\n")
    print(f"A palavra era {palavra_secreta}\n")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Se o arquivo aberto for o arquivo principal rodar a função jogar()
if(__name__ == "__main__"):
    jogar()