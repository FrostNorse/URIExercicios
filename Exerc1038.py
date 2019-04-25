valores = [4.00, 4.50, 5.00, 2.00, 1.50]
codigo, quantidade = map(int, input().split())
print("Total: R$ %.2F" % (valores[codigo-1] * quantidade))
