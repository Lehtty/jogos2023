import random


def jogar():

    msg_inicio()
    msg_escolha()

    palavra_secreta = int(input("Categoria: "))
    if (palavra_secreta == 1):
        palavra_secreta = frutas()
    elif (palavra_secreta == 2):
        palavra_secreta = flores()
    else:
        palavra_secreta = nomes()

    letras_acertadas = inicializa_letras(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not acertou and not enforcou):

        chute = l_chutada()

        if (chute in palavra_secreta):
            chutou_certo(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print(f"Errou, faltam somente {7 - erros} tentativas")
            forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        if not acertou and not enforcou:
            print("Jogando...")

    if(acertou):
        ansi_venceu(palavra_secreta)
    else:
        ansi_enforcou(palavra_secreta)

    msg_finalizacao()



def msg_escolha():
    print("Escolha um categoria: ")
    print("[1] Frutas [2] Flores [3] Nomes")

def msg_inicio():
    print("                                 ")
    print("***Bem-vindo ao jogo da forca!***")
    print("                                 ")

def frutas():
    arquivo = open("frutas.txt", "r")
    frutas = []

    for linha in arquivo:
        linha = linha.strip()
        frutas.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(frutas))
    palavra_secreta = frutas[numero].upper()
    return palavra_secreta

def flores():
    arquivo = open("flores.txt", "r")
    flores = []

    for linha in arquivo:
        linha = linha.strip()
        flores.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(flores))
    palavra_secreta = flores[numero].upper()
    return palavra_secreta

def nomes():
    arquivo = open("nomes.txt", "r")
    nomes = []

    for linha in arquivo:
        linha = linha.strip()
        nomes.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(nomes))
    palavra_secreta = nomes[numero].upper()
    return palavra_secreta

def inicializa_letras(palavra):
    return ["_" for letra in palavra]

def l_chutada():
    chute = input("Sua letra: ")
    chute = chute.strip().upper()
    return chute

def chutou_certo(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1    

def ansi_venceu(palavra_secreta):
    print('  ************  Parabéns  ************  ')
    print('                                        ')
    print('            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓           ')
    print('             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ')
    print('           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ')
    print('           ▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓          ')
    print('            ▓ ▓▓▓▓▓▓▓▓▓▓▓▓▒ ▓           ')
    print('             ▓ ▓▓▓▓▓▓▓▓▓▓▓▒▓            ')
    print('               ▓▓▓▓▓▓▓▓▓▓▓              ')
    print('                  ▓▓▓▓▓                 ')
    print('                   ▓▓▓                  ')
    print('                ▓▓▓▓▓▓▓▓▓               ')
    print('                ▓▓▓▓▓▓▓▒▓               ')
    print('                ▓▓▓▓▓▓▓▓▓               ')
    print('                ▓▓▓▓▓▓▓▓▓               ')
    print('               ▓▓▓▓▓▓▓▓▓▓▓              ')

def ansi_enforcou(palavra_secreta):
    print('********* Se Ferrou *********')
    print(" ███████████████████████████ ")
    print(" ███████▀▀▀░░░░░░░▀▀▀███████ ")
    print(' ████▀░░░░░░░░░░░░░░░░░▀████ ')
    print(' ███│░░░░░░░░░░░░░░░░░░░│███ ')
    print(' ██▌│░░░░░░░░░░░░░░░░░░░│▐██ ')
    print(' ██░└┐░░░░░░░░░░░░░░░░░┌┘░██ ')
    print(' ██░░└┐░░░░░░░░░░░░░░░┌┘░░██ ')
    print(' ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██ ')
    print(' ██▌░│██████▌░░░▐██████│░▐██ ')
    print(' ███░│▐███▀▀░░▄░░▀▀███▌│░███ ')
    print(' ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██ ')
    print(' ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██ ')
    print(' ████▄─┘██▌░░░░░░░▐██└─▄████ ')
    print(' █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████ ')
    print(' ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████ ')
    print(' █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████ ')
    print(' ███████▄░░░░░░░░░░░▄███████ ')
    print(' ██████████▄▄▄▄▄▄▄██████████ ')
    print(' ███████████████████████████ ')

def forca(erros):

    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
         print(" |      (_)   ")
         print(" |      \|/   ")
         print(" |            ")
         print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
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

def msg_finalizacao():
    print("                        ")
    print("***** Fim de jogo! *****")
    print("                        ")    

if (__name__ == "__main__"):
    jogar()