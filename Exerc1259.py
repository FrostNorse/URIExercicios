linhas = int(input())
par = []
impar = []
for i in range(linhas):
    numero = int(input())
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
par.sort()
impar.sort()
impar.reverse()
par.extend(impar)
for i in par:
    print(i)
