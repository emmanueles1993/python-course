import random

def generar_contrasena():
    mayusculas = ["A" , "B" , "C" , "D" , "E" , "F" , "G"]
    minusculas = ["a" , "b" , "c" , "d" , "e" , "f" , "g"]
    simbolos = ["!" ,"@" , "'" , "¡" , "(" , ")"]
    numeros = ["1" , "2" , "3" , "4" , "5" , "6"]

    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres) # .choice elige un caraceter al azar de toda la lista de caracteres
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena) # covierte la lista a un string "".join(lista original)se crea la cadena
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("tu nueva contraseña es :" + contrasena)
    


if __name__ == "__main__":
    run()



