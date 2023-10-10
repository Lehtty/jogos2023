import forca
import adivinhacao

def escolha_de_jogo():
    print("                      ")
    print(" ******************** ")
    print(" * Escolha um jogo! * ")
    print(" *********************")
    print("                      ")

    print("(1) - Forca")
    print("(2) - Adivinhação")

    jogo = int(input("Qual jogo você deseja jogar?"))

    if (jogo == 1):
        print("Executando o jogo da Forca...")
        forca.jogar()
    elif (jogo == 2):
        print("Executando jogo da Adivinhação...")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolha_de_jogo()