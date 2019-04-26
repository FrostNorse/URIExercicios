quantidadeSoldado, pulo = map(int, input().split())
soldado = []
soldadoAtual = 0
for i in range(quantidadeSoldado):
    soldado.append(i+1)
while len(soldado) > 1:
    soldadoAtual += pulo-1
    if soldadoAtual > len(soldado):
        soldadoAtual %= len(soldado)
    soldado.remove(soldado[soldadoAtual])
print(soldado[0])


