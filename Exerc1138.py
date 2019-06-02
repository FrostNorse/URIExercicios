inicio, fim = map(int, input().split())
num = inicio
digitos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while num <= fim:
    numero = str(num)
    for i in numero:
        digitos[int(i)] += 1
    num += 1
print(str(digitos).strip("[]"))

