while True:
    try:
        num1, num2 = map(int, input().split())
        num1 = int(bin(num1).replace("0b", ""))
        num2 = int(bin(num2).replace("0b", ""))
        soma = str(num1 + num2)
        soma = soma.replace("2", "0")
        print(int(soma, 2))
    except EOFError:
        break
