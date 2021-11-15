codigo_da_peca1, numero_de_pecas1, valor_unitario1 = input().split()
codigo_da_peca2, numero_de_pecas2, valor_unitario2 = input().split()
preco = int(numero_de_pecas1) * float(valor_unitario1) + int(numero_de_pecas2) * float(valor_unitario2)
print("VALOR A PAGAR: R$ %.2f" % preco)