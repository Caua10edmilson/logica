palavra=str(input("Digite uma palavra"))
contador=0

for letra in palavra:
    if letra in "aeiou":
        contador += 1
print(f"a palavra{palavra} possui {contador} vogais ")
