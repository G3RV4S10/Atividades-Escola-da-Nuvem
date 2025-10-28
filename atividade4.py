"""
Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
qtd = 3

valor_total = preco_unitario * qtd

print(f"Nome do Produto: {nome_produto}")
print(f"Preço por unidade: R$ {preco_unitario:,.2f}")
print(f"Quantidade: {qtd}")
print("---")

print(f"Total a pagar: R$ {valor_total:,.2f}")