# sep="" serve para adicionar um separador
#print("Brasil", "ganhou", 5, "titulos", "mundiais", sep="-")
# end="" para adiconar ao final
#print("Brasil", "ganhou", 5, "titulos", "mundiais", end="-")
# no python o tipo da variavel é auto-identificada, não há necessidade de colocar o tipo

#Console.Write()
print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

# input = Console.Read()
# colocamos a variavel junto da pergunta
chute_str= input("Digite o seu numero: ")
print("Você digitou: ", chute_str)

# métopdo de conversao
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

print("Fim do jogo")
