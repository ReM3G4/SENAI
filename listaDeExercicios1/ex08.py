nota = int(input("Insira a nota(0 a 10):"))

if nota >= 7:
    print("Aprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
else:
    print("Reprovado")
