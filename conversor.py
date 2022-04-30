# pesos = input("¿cuantos pesos colombianos tienes?: ")
# pesos= float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("tienes $" + dolares + " dolares")


# pesosmex = input("ingrese valor de pesos mexicanos: ")
# pesosmex = float(pesosmex)
# valordolar = 20.42
# dolares = pesosmex/valordolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("usted tiene en dolares:" + " " +dolares)

# dolar =input("¿cuantos dolares tienes? ")
# dolar = float(dolar)
# valorpesosmex = 0.049
# pesosmex = dolar / valorpesosmex
# pesosmex =  round(pesosmex ,2)
# pesosmex = str(pesosmex)
# print("usted tiene en pesos mexicanos" + ": " + pesosmex)

def conversor(tipo_pesos, valor_dolar):
   pesos = input("¿cuantos pesos " +tipo_pesos + "tienes?: ")
   pesos= float(pesos)
   dolares = pesos / valor_dolar
   dolares = round(dolares, 2)
   dolares = str(dolares)
   print("tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de moneda 💲
1- pesos colombianos
2- pesos mexicanos
3- pesos argentinos

Elige una opcion:"""

opcion = int(input(menu))

if opcion == 1:
  conversor("colombianos " , 3875)
elif opcion == 2:
  conversor("argentinos " , 65)
elif opcion == 3:
  conversor("mexicanos " , 24)

else:
    print("Ingresa una opcion correcta por favor")


