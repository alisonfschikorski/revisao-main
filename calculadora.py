while True:
    menu = """=============CALCULADORA=========== 
            1 - SOMA (+)
            2 - SUBTRACAO (-)
            3 - MULTIPLICACAO(X)
            4 - DIVISAO(\)
            0 - SAIR
            """
    print(menu)
    escolhe = input("digite a opção")       
    n1= input ("digite o primeiro numero")
    n2 = input("digite o segundo numero") 
    
    if escolhe == "1":
     total= n1 + n2 
    print(f"sua conta deu:{total}")
    
    if escolhe == "2": 
     total= n1 - n2 
     print(f"sua conta deu:{total}")

     if escolhe == "3":
       total= n1 * n2
       print(f"sua conta deu: {total}")

       if escolhe == "4":
         total= n1 / n2 
         print(f"seu total foi:{total}")
         
     