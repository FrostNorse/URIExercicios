reais, centavos = map(int, input().split("."))
print("NOTAS:")
print("%d nota(s) de R$ 100.00" % (reais / 100))
reais %= 100
print("%d nota(s) de R$ 50.00" % (reais / 50))
reais %= 50
print("%d nota(s) de R$ 20.00" % (reais / 20))
reais %= 20
print("%d nota(s) de R$ 10.00" % (reais / 10))
reais %= 10
print("%d nota(s) de R$ 5.00" % (reais / 5))
reais %= 5
print("%d nota(s) de R$ 2.00" % (reais / 2))
centavos += (reais % 2) * 100
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % (centavos / 100))
centavos %= 100
print("%d moeda(s) de R$ 0.50" % (centavos / 50))
centavos %= 50
print("%d moeda(s) de R$ 0.25" % (centavos / 25))
centavos %= 25
print("%d moeda(s) de R$ 0.10" % (centavos / 10))
centavos %= 10
print("%d moeda(s) de R$ 0.05" % (centavos / 5))
print("%d moeda(s) de R$ 0.01" % (centavos % 5))
