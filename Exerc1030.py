teste = int(input())
for i in range(teste):
    quantidadeSoldado, pulo = map(int, input().split())
    soldado = []
    soldadoAtual = pulo-1
    for j in range(quantidadeSoldado):
        soldado.append(j+1)
    while len(soldado) > 1:
        soldado.remove(soldado[soldadoAtual])
        soldadoAtual += pulo-1
        if soldadoAtual >= len(soldado):
            soldadoAtual %= len(soldado)
    print("Case %d: %d" % (i+1, soldado[0]))
