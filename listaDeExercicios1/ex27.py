ttry = 3

while ttry > 0:
    login = input("Insira o login: ")
    senha = input("Insira a senha: ")

    if login == "admin" and senha == "1234":
        print("Login realizado com sucesso")
        break

    else:
        ttry -= 1
        print("Credenciais inválidas,", ttry, "tentativas restantes.")

if ttry == 0:
    print("Número máximo de tentativas atingido.")
