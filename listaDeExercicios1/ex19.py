n1 = int(input("Coloque um preço: "))
n2 = int(input("Coloque um preço: "))
n3 = int(input("Coloque um preço: "))
n4 = int(input("Coloque um preço: "))
n5 = int(input("Coloque um preço: "))

subtotal = float(n1 + n2 + n3 + n4 + n5)
total = float(n1 + n2 + n3 + n4 + n5) * 1.10

print("Seu subtotal é: ", str(subtotal),". Com os 10% de imposto ficou: ", str(total), "." )
