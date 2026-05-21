idade = -1  

while idade < 0 or idade > 120:
    idade = int (input("digite uma idade valida (0 a 120): "))
    if idade < 0 or idade > 120:
        print ("idade invalida! tente novamente.")

print(f"obrigado! parabens! a idade digitada foi {idade}")
