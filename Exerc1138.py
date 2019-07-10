while True:
    inicio, fim = map(int, input().split())
    if inicio == 0 and fim == 0:
        break
    num = inicio
    digitos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while num <= fim:
        numero = str(num)
        for i in numero:
            digitos[int(i)] += 1
        num += 1
    print(str(digitos).strip("[]").replace(",", ""))
