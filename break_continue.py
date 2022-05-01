# #imprimir numeros pares
# def run():
 
#     for contador in range(1000): # del 0 al 999
#         if contador % 2 != 0: #si es diferente a 0  se encuentra aqui con esta variable siendo un numero impar, saltamos las vueltas del ciclo y no imprimimos ese contador
#             continue
#         print(contador)


# if __name__ == "__main__":  
#  run()
def run():
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    texto = input("Escribe el texto : ")
    for letra in texto:
        if letra == "o":
           break
        print(letra)
        


if __name__ == "__main__":
        run()