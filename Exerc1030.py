case = int(input())
for j in range(0, case):
    quantidadeSoldado, pulo = map(int, input().split())
    soldados = []
    soldadosvivos = quantidadeSoldado
    soldadoatual = 1
    puloatual = 0
    for i in range(0, quantidadeSoldado):
        soldados.append(i + 1)
    while soldadosvivos != 1:

        if soldadoatual > quantidadeSoldado:
            soldadoatual -= quantidadeSoldado

        if soldados[soldadoatual - 1] > 0:
            puloatual += 1

        if puloatual == pulo:
            soldados[soldadoatual - 1] = 0
            puloatual = 0
            soldadosvivos -= 1

        soldadoatual += 1

    for i in soldados:
        if i > 0:
            print("Case {}:".format(j+1), i)
