nome = input("insira o nome do produto: ")
qa = int(input("Insira a quantidade atual: "))
qv = int(input("Insira a quantidade vendida: "))

estoque = qa - qv

if estoque<= 0:
    print("Alerta! O item falta no estoque! estoque atual: ", estoque)
else:
    print("quantidade de itens restantes: ", estoque)
