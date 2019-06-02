dias = int(input())
casa = 0
escritorio = 0
totalEscritorio = 0
totalCasa = 0
for i in range(dias):
    dia = list(map(str, input().split()))
    if dia[0] == "chuva":
        if casa == 0:
            escritorio += 1
            totalCasa += 1
        else:
            escritorio += 1
            casa -= 1
    if dia[1] == "chuva":
        if escritorio == 0:
            casa += 1
            totalEscritorio += 1
        else:
            casa += 1
            escritorio -= 1
print(totalCasa, totalEscritorio)
