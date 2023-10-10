import random

def jogar():

    print('                                               ')
    print('  ***** Bem vindo ao jogo de Adivinhação! *****')
    print('                                               ')

    numero_secreto = random.randrange(1,101)
    total_de_vezes = 0
    pontos = 1000

    print("Qual dificuldade deseja?")
    print("(1) - Fácil")
    print("(2) - Moderado")
    print("(3) - Dificíl")
    nivel = int(input("Escolha de dificulcudade: "))

    if(nivel == 1):
        total_de_vezes = 20
    elif(nivel == 2):
        total_de_vezes = 10
    else:
        total_de_vezes = 5

    for rodada in range(1, total_de_vezes + 1):
        print(f'Tentativa: {rodada} de {total_de_vezes}')
        chute_numero = input("Digite seu número: ")
        print("Você digitou: ", chute_numero)
        chute = int(chute_numero)

        if(chute < 1 or chute > 100):
            print("O número deve estar entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f'Acertou, você fez {pontos} pontos!')
            break
        else:
            if(maior):
                print("Você errou! O número secreto é menor!")
                if (rodada == total_de_vezes):
                    print(f'O número era {numero_secreto}, você fez {pontos}, mais sorte a próxima vez!')
            elif(menor):
                print("Você errou! O número secreto é maior!")
                if (rodada == total_de_vezes):
                    print(f'O número secreto era {numero_secreto}, você fez {pontos}, mais sorte a próxima vez!')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("                            ")
    print("  ***** Fim de jogo! *****  ")
    print("                            ")

if(__name__ == "__main__"):
    jogar()                                      