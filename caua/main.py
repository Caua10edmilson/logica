#nome = "Maria"

#for letra in nome:
#   print(letra)
#    print("Texto qualquer")

palavra = str(input("Digite uma palavra:")).lower()
tem_a_letra_A = False
quantidade = 0


for letra in palavra:
    if letra == "a":
        tem_a_letra_A = True
        quantidade = quantidade + 1

if tem_a_letra_A == True:
    print(f"Sua palavra possui {quantidade} letras A")
else:
    print("Sua palavra nao possui a letra A")
