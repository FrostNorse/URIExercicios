num = float(input())
if num < 0 or num >100:
    print("Fora de intervalo")
else:
    num = num/25
    if num <= 1:
        print("Intervalo [0,25]")
    elif num <= 2:
        print("Intervalo (25,50]")
    elif num <= 3:
        print("Intervalo (50,75]")
    else:
        print("Intervalo (75,100]")
