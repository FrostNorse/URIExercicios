while True:
    numregiao = int(input())
    if numregiao == 0:
        break
    pulo = 1
    regiaoAtual = 0
    while True:
        regioes = list(range(1, numregiao + 1))
        while len(regioes) > 1:
            regioes.remove(regioes[regiaoAtual])
            regiaoAtual += pulo - 1
            if regiaoAtual >= len(regioes):
                regiaoAtual %= len(regioes)
        if regioes[0] == 13:
            resposta = pulo
            break
        else:
            pulo += 1
    print(resposta)
