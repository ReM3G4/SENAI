MB = float(input("insira o tamanho do arquivos em MB. (insira somente números) \n"))
NET = float(input("insira a velocidade do link de internet em Mbps. (insira somente números) \n"))
download = MB * 8 / NET
print ("Demorará ", download," segundos para o seu download.")
