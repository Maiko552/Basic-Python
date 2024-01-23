
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#random range
numero_secreto = round(random.randrange(1,101)) 
total_de_tentativas = 3
rodada = 1

# +1 no final, de 1 a 10 ele imprime 9
for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        #mesmo se a pessoa digitar 0 nao vai parar o codigo
        
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        #ponto de parada
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

    

print("Fim do jogo")