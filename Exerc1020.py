inicial = int(input())
anos = inicial / 365
inicial %= 365
meses = inicial / 30
inicial %= 30
print("%d ano(s)" % anos)
print("%d mes(es)" % meses)
print("%d dia(s)" % inicial)
