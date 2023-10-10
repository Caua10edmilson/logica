letra = str(input("Digite uma letra: ")).lower()

if len(letra) ==1:
   if letra in "aeiou":
    print("Vogal")
if letra in "qwrtyopsdfghjklmnbvcxz":
    print("consoante")
else:
    print("Digite uma LETRA")


    