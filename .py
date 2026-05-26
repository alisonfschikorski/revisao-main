produtos = ["Pneu", "Bateria", "Óleo de Motor", "Palheta"]
precos_produtos = [450.00, 320.00, 150.00, 45.00]

servicos = ["Alinhamento", "Revisão Geral", "Lavagem Completa", "Troca de Filtro"]
precos_servicos = [120.00, 350.00, 80.00, 50.00]

escolha_categoria = input("Você deseja ver nossos Produtos ou Serviços? ").strip().capitalize()

item_escolhido = ""
preco_original = 0.0

if escolha_categoria == "Produto" or escolha_categoria == "Produtos":
    print("\n--- PRODUTOS DISPONÍVEIS ---")
  
    for i, prod in enumerate(produtos):
        print(f"[{i}] {prod} - R$ {precos_produtos[i]:.2f}")
        
    # 4. Escolha do item pelo índice
    indice = int(input("\nDigite o número do produto que deseja comprar: "))
    item_escolhido = produtos[indice]
    preco_original = precos_produtos[indice]

elif escolha_categoria == "Serviço" or escolha_categoria == "Serviços" or escolha_categoria == "Servico":
    print("\n--- SERVIÇOS DISPONÍVEIS ---")
    for i, serv in enumerate(servicos):
        print(f"[{i}] {serv} - R$ {precos_servicos[i]:.2f}")
        
    indice = int(input("\nDigite o número do serviço que deseja contratar: "))
    item_escolhido = servicos[indice]
    preco_original = precos_servicos[indice]

else:
    print("Opção inválida! Reinicie o programa.")
    exit()

desconto = 0.0
if preco_original > 300.00:
    desconto = preco_original * 0.10

preco_final = preco_original - desconto


print("\n" + "="*30)
print("          CUPOM FISCAL         ")
print("="*30)
print(f" Item: {item_escolhido}")
print(f" Valor Original: R$ {preco_original:.2f}")

if desconto > 0:
    print(f" Desconto (10%): R$ {desconto:.2f}")
    
print("-" * 30)
print(f" TOTAL A PAGAR:  R$ {preco_final:.2f}")
print("="*30)
print("    Obrigado pela preferência!   ")
print("="*30)