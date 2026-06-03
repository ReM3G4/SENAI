total =  float(input("insira o valor atual da bolsa do estagiário: "))
if total >= 1000:
    total = total+total*0.10
else:
    total = total+total*0.15
print ("total: ",total)
