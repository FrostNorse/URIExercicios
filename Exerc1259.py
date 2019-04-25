numLine = int(input())
pair = []
impair = []
for i in range(numLine):
    digit = int(input())
    if digit % 2 == 0:
        pair.append(digit)
    else:
        impair.append(digit)
pair.sort()
impair.sort()
impair.reverse()
pair.extend(impair)
for i in pair:
    print(i)