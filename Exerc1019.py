inicial = int(input())
horas = inicial / 3600
inicial %= 3600
minutos = inicial / 60
inicial %= 60
print("%d:%d:%d" % (horas, minutos, inicial))
