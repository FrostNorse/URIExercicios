teste = int(input())
for k in range(teste):
    tamanho = int(input())
    sequencia = list(map(int, input().split()))
    i = 0
    while True:
        if i >= len(sequencia):
            break
        if sequencia[i] % 2 == 0:
            sequencia.pop(i)
        else:
            i += 1
    maior = []
    menor = []
    sequencia.sort()
    while len(sequencia) != 0:
        try:
            maior.append(sequencia.pop(len(sequencia)-1))
            menor.append(sequencia.pop(0))
        except:
            break
    index = 1
    for i in menor:
        maior.insert(index, i)
        index += 2
    print(str(maior).strip("[]").replace(",", ""))