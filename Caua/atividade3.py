cor = str(input("escolha uma cor entre verde amarelo e vermelho:").lower().strip())

# if cor == "verde":
#     print("acelera")
# if cor == "amarelo":
#     print("atenção")
# if cor== "vermelho":
#     print("Pare")
# else:
#     print("Cor invalida")


match cor:
    case "vermelho":
         print("Pare")
    case "verde":
         print("acelera")
    case "amarelo":
         print ("atenção")
    case _:
          print("invalido")    


         