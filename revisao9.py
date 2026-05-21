produtos = ["miojo" , "pao"  , "suco"]
precos = [5.00, 9.00, 3.00]

for posicao_produto, produtos in enumerate (produtos):
    print(f"produto: {produtos} custa R${precos[posicao_produto]}")

if precos[posicao_produto]: