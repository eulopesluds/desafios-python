n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

average = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print("Media: {:.1f}".format(average))

if average >= 7:
    print("Aluno aprovado.")
elif average < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    n5 = float(input())

    average = (n5 + average) / 2

    print("Nota do exame: {:.1f}".format(n5))

    if average >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")


    print("Media final: {:.1f}".format(average))
