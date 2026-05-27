notas = []

for i in range (10):
    nota = int(input("adicione a nota: "))
    notas.append(nota)

lista_crescente = sorted(notas)
print ("Crescente: ", lista_crescente)
lista_decrescente = sorted(notas, reverse=True)
print ("decrescente: ", lista_decrescente)

