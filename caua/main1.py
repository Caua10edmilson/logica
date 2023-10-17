#alfabeto ="abcdefghijklmnopqrstuvwxy"

#for letra in alfabeto:
 #   if letra not in "aeiou":
#        print(letra)

palavra = str(input("Digite uma frase com numero:")).lower()
contem_numero = False
quantidade=0

for numero in palavra:
    if numero in "0123456789":
        contem_numero=True
        quantidade=quantidade+1


if contem_numero==True:
    print(f"Sua frase tem os numeros {quantidade}")
else:
    print("Sua frase nao tem numero")

