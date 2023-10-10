alternativa = str(input("Qual o seu sexo biologico F/M:")).lower()

if alternativa == "f" or alternativa == "m":
    if alternativa == "f":
        print("Seu sexo e feminino")
    else:
        print("Seu sexo e masculino")
else:
    print("Operação invalida")


