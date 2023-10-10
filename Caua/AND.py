alternativa = str(input("Voce  deseja sair? S/N")).lower()


if alternativa == "s" or alternativa == "n":
    print("Operação valida")
    if alternativa == "s":
        print("Tchau meu fih,vai com deus")
    else:
        print("Continue usando o programa")
else:
    print("Operação invalida")
            
