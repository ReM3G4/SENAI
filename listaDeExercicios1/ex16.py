senha = input("Insira a senha (minimo 8 caracteres): ")

while len(senha) < 8:
    print ("senha invalida.")
    senha = input("Insira a senha (minimo 8 caracteres): ")
print("senha válida.")
