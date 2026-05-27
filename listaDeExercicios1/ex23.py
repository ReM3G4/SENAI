vendas = []


def inserir():
    venda = int(input("Quantas vendas foram hoje?: "))
    vendas.append(venda)


def receita():
    print(vendas)
    maior_venda = max(vendas)
    menos_venda = min(vendas)
    dias = len(vendas)
    total = sum(vendas)
    media = float(total)/dias
    print("maior venda: ", maior_venda)
    print("menor venda: ", menos_venda)
    print("total de vendas: ", dias, "lucro total: ",total)
    print("media :", media)

def sair():
    print("Você saiu.")


while True:
        print("\n === Menu de vendas ===")
        print("1 - inserir vendas")
        print("2 - Receita")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir()

        elif opcao == "2":
            receita()

        elif opcao == "3":
            sair()

        else:
            print("mensagem inválida")
