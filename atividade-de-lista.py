produtos = ["camiseta","calca","touca","casaco","tenis"]
precos = [40.00, 50.00, 45.00, 100.00, 120.00]
quantidades =  [2, 1, 2, 1, 1]
subtotais = []
#ANTES, FARIA ASSIM PARA PEGAR O PRODUTO E O PREÇO:

print(f"o produto {produtos[0]} custa R${precos[0]}")

for indice, produtos in enumerate (produtos):
    preco = precos[indice] # preço= precos [0] 
    quantidade = quantidades[indice]
    subtotal = quantidade * preco
    subtotais.append(subtotal)


    mensagem = f"""
    ---------------------------------
    produto: {produtos}
    quantidade: {quantidade}
    valor unitario: {precos}
    sbutotal: {subtotal}
    ---------------------------------
    """
    print(mensagem)


print(f"O total da compra deu: R${sum(subtotais)}")