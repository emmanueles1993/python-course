def run ():
#     mi_diccionario = {
#         "lista1" : 1,
#         "lista2" : 2,
#         "lista3" : 3,

# }
#     print(mi_diccionario["lista1"])

    poblacion = {
     "argentina" : 2000000,
     "bolivia" : 3000000,
     "colombia" : 400000,
    }
    # for pais in poblacion.keys():
    #     print(pais)

    # for pais in poblacion.values():
    #     print(pais)
    for pais, poblacion1 in poblacion.items():
        print(pais +" tiene " + str(poblacion1) + " habitantes" )

    # print(poblacion["colombia"])

if __name__ == "__main__":
    run()