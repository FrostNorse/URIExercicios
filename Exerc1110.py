while True:
    numerocartas = int(input())
    if numerocartas == 0:
        break
    pilhacartas = []
    for i in range(0, numerocartas):
        pilhacartas.append(i+1)
    cartasRetiradas = []
    while len(pilhacartas) != 1:
        cartasRetiradas.append(pilhacartas.pop(0))
        pilhacartas.insert(len(pilhacartas)-1, pilhacartas.pop(0))
    print("Discarded cards: " + str(cartasRetiradas).replace("[", "").replace("]", ""))
    print("Remaining card: " + str(pilhacartas[0]))
