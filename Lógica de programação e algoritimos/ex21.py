pares = 0
impares = 0

for i in range(10):
    numero = int(input("Insira um número inteiro: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Desses números, ", pares, " são pares e ", impares, " são impares.")
