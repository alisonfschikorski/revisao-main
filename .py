produtos = ["Pneu", "Bateria", "Óleo de Motor", "Palheta"]
precos_produtos = [450.00, 320.00, 150.00, 45.00]

servicos = ["Alinhamento", "Revisão Geral", "Lavagem Completa", "Troca de Filtro"]
precos_servicos = [120.00, 350.00, 80.00, 50.00]
escolha_categoria = input("Você deseja ver nossos Produtos ou Serviços?")

opcao = input("Você deseja ver nossos Produtos ou Serviços? ")

print("\n--- OPÇÕES DISPONÍVEIS ---")

if opcao == "Produto" or opcao == "Produtos":
    for indice, item in enumerate(produtos):
        preco = precos_produtos[indice]
    print(f"{indice} - {item} - R$ {preco:.2f}")

elif opcao == "Serviço" or opcao == "Servico" or opcao == "Serviços":
    for indice, item in enumerate(servicos):
        preco = precos_servicos[indice]
        print(f"{indice} - {item} - R$ {preco:.2f}")

else:
    print("Opção inválida! Por favor, reinicie e digite 'Produto' ou 'Serviço'.")
  
escolha_indice = int(input("\nDigite o número do item que você deseja: "))

if opcao == "Produto" or opcao == "Produtos":
    item_escolhido = produtos[escolha_indice]
    preco_original = precos_produtos[escolha_indice]

elif opcao == "Serviço" or opcao == "Servico" or opcao == "Serviços":
    item_escolhido = servicos[escolha_indice]
    preco_original = precos_servicos[escolha_indice]

print(f"\nVocê selecionou: {item_escolhido} (Valor original: R$ {preco_original:.2f})")

#  REGRA DE DESCONTO 
valor_final = preco_original

if preco_original > 300.00:
    desconto = preco_original * 0.10  # Calcula 10% de desconto
    valor_final = preco_original - desconto
    print(f"Parabéns Você ganhou 10% de desconto. Economizou: R$ {desconto:.2f}")
else:
    print("Este item não possui desconto promocional.")

print("\n" + "="*30)
print("       CUPOM FISCAL       ")
print("="*30)
print(f" Item: {item_escolhido}")
print(f" Valor Orig: R$ {preco_original:.2f}")

# mostrando o valor final com o desconto aplicado
if preco_original > 300.00:
    desconto_aplicado = preco_original * 0.10
    print(f" Desconto:  -R$ {desconto_aplicado:.2f} (10%)")

