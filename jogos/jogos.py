'''
    Arquivo de inicialização que pergunta qual jogo o usuário gostaria de entrar.
'''

import forca
import advinhacao

def escolher_jogo():

    print("\n*********************************")
    print("****** Escolha o seu jogo! ******")
    print("*********************************\n")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    # Condição de escolha dos jogos
    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        advinhacao.jogar()

# Se o arquivo aberto for o arquivo principal rodar a função jogar()
if(__name__ == "__main__"):
    escolher_jogo()