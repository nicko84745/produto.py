nome_produto = input("digite o nome do preço: ")
preço = float(input("digite o preço do produto:"))
desconto = float(input("digite o percentual de desconto "))
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto
print(f"produto: {nome_produto} - preço final: R$ {preco_final}")