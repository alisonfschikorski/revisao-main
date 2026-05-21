import random

numero_secreto = random.randint(1,10) 
palpite  = 0 
tentativas = 0

while palpite != numero_secreto:
    palpite = int (input("adivinhe o numero (1 a 10): "))
    if palpite != numero_secreto:
        print("errou! tente novamente.")

    tentativas = tentativas + 1 


print(f"acertou! parabens! voce tentou {tentativas} vezes.")
