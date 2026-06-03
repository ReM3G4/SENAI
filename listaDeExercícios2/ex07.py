oc = int(input("Insira o primeiro octeto de seu endereço IP (ex: o 192 de 192.168.0.1)."))

if oc >=126:
    print("Classe A")
elif oc <= 128 and oc>= 191:
    print("Classe B")
elif oc <= 192 and oc >= 223 :
    print("Classe C")
else:
    print("Classe não registrada.")
