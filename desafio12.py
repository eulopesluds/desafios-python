nota_x = int(input())
nota_original = nota_x
# declarando a quantidade inicial das notas
nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

while nota_x > 0:
    if nota_x >= 100:
        nota_100 = nota_100 + 1
        nota_x = nota_x - 100
    elif nota_x >= 50:
        nota_50 = nota_50 + 1
        nota_x = nota_x - 50
    elif nota_x >= 20:
        nota_20 = nota_20 + 1
        nota_x = nota_x - 20
    elif nota_x >= 10:
        nota_10 = 10 +1
        nota_x = nota_x - 10
    elif nota_x >= 5:
        nota_5 = nota_5 + 1
        nota_x = nota_x - 5
    elif nota_x >= 2:
        nota_2 = nota_2 +1
        nota_x = nota_x - 2
    else:  # se nao for nenhum dos de cima so pode ser 1
        nota_1 = nota_1 + 1
        nota_x = nota_x - 1

print(nota_original)
print(f"{nota_100} nota(s) de R$ 100,00")
print(f"{nota_50} nota(s) de R$ 50,00")
print(f"{nota_20} nota(s) de R$ 20,00")
print(f"{nota_10} nota(s) de R$ 10,00")
print(f"{nota_5} nota(s) de R$ 5,00")
print(f"{nota_2} nota(s) de R$ 2,00")
print(f"{nota_1} nota(s) de R$ 1,00")