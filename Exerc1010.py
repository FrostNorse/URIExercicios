linha1=input().split()
linha2=input().split()
Code1, Value1, Quant1 = linha1
Code2, Value2, Quant2 = linha2
print("VALOR A PAGAR: R$ %.2F" % ((int(Value1) * float(Quant1)) + (int(Value2) * float(Quant2))))
