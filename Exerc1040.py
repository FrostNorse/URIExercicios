n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print("Media: %.1F" % media)
if media >= 7:
    print("Aluno aprovado.")
elif 6.9 >= media >= 5:
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: %.1F" % notaExame)
    media += notaExame
    media /= 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1F" % media)
else:
    print("Aluno reprovado.")
