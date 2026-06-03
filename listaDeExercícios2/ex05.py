price = float(input("Insira o total do livro."))
if price > 80:
    price = price - (price * 0.10)
    print("Desconto aplicado, total: ", price)
else:
    print("Total :", price )
