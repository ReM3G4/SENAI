total = []
resp = ""
while resp != "sair":
    its = input("Qual item você gostaria de comprar? \n")
    total.append(its)
    resp = input("Irá continar comprando? Caso não, digite: (sair)")
print(total)
