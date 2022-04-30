def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" " , "")
    palabra_invertida = palabra[::-1]
    if palabra_invertida == palabra:
        return True
    else:
        return False


def run ():
    palabra = input("Escribe tu palabra :")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es un palindromo")
    else:
        print("No es un palindromo")

if __name__ == '__main__':
    run()


