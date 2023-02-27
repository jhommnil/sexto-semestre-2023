def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def validaCero(divisor):
    if (divisor == 0):
        print("Error: El divisor no puede ser cero.")
        return leerEntero("  Nuevo divisor (0 para salir):")
    else:
        return divisor


'''def valNull():
    num1 = leerEntero("Num1:")
    if num1 is None:
        print("Error: No se pudo leer un número válido.")

    num2 = leerEntero("Num2:")
    if num2 is None:
        print("Error: No se pudo leer un número válido.")

    print("La suma es:", suma(num1, num2))'''
def leerEntero(mensaje):
    contador = 0
    while contador < 3:
        try:
            return int(input(mensaje))
        except:
            print(": Entero no válido..")
            contador = contador + 1
    print("Se superó el número máximo de intentos fallidos.")
    return None
'''def leerEntero(mensaje):
    contador = 0
    while contador < 3:
        try:
            return int(input(mensaje))
        except:
            print(": Entero no válido..")
            contador = contador + 1'''

def menu():
    print("0- Salir")
    print("1- suma")
    print("2- resta")
    print("3- multiplicacion")
    print("4- division")
    return leerEntero("  >> Ingrese una opcion:")
'''def main():
    while True:
        opcion = menu()
        print("Opcion = ", opcion)
        if (opcion==0):
            break
        else:
            match(opcion):
                case 0:
                    print("Sali!!!! rata Gaaaaaa")
                case 1:
                    print("La suma es:", suma(valNull(leerEntero("Num1:"), leerEntero("Num2:"))))
                case 2:
                    print("La resta es:", resta(leerEntero("Num1:"), leerEntero("Num2:")))
                case 3:
                    print("La multiplicacion es:", multiplicacion(leerEntero("Num1:"), leerEntero("Num2:")))
                case 4:
                    num1 = leerEntero("Num1:")
                    num2 = validaCero(leerEntero("Num2:"))
                    opcion = menu()
                    if (num2 != 0):
                        print("La division es:",division(num1, num2))
                    else:
                        print("El divisor sigue siendo cero. Regresando al menu.")'''

def main():
    while True:
        opcion = menu()
        print("Opcion = ", opcion)
        if (opcion==0):
            break
        else:
            match(opcion):
                case 0:
                    print("Sali!!!! rata Gaaaaaa")
                case 1:
                    num1 = leerEntero("Num1:")
                    if num1 is None:
                        print("Error: No se pudo leer un número válido.")
                        continue
                    num2 = leerEntero("Num2:")
                    if num2 is None:
                        print("Error: No se pudo leer un número válido.")
                        continue
                    print("La suma es:", suma(num1, num2))
                case 2:
                    num1 = leerEntero("Num1:")
                    if num1 is None:
                        print("Error: No se pudo leer un número válido.")
                        continue
                    num2 = leerEntero("Num2:")
                    if num2 is None:
                        print("Error: No se pudo leer un número válido.")
                        continue
                    print("La resta es:", resta(num1, num2))
                case 3:
                    num1 = leerEntero("Num1:")
                    if num1 is None:
                        print("Error: No se pudo leer un número válido.")
                        continue
                    num2 = leerEntero("Num2:")
                    if num2 is None:
                        print("Error: No se pudo leer un número válido.")
                        continue
                    print("La multiplicacion es:", multiplicacion(num1, num2))
                case 4:
                    num1 = leerEntero("Num1:")
                    if num1 is None:
                        print("Error: No se pudo leer un número válido.")
                        continue
                    num2 = validaCero(leerEntero("Num2:"))
                    if num2 is None:
                        print("Error: No se pudo leer un número válido.")
                        continue
                    # num1 = leerEntero("Num1:")
                    # num2 = validaCero(leerEntero("Num2"))
                    if (num2 != 0):
                        print(division(num1, num2))
                    else:
                        print("El divisor sigue siendo cero. Regresando al menu.")
main()
    # if opcion == 1:
        #     print("La suma es:",suma(leerEntero("Num1:"), leerEntero("Num2:")))
        # elif opcion == 2:
        #     print("La resta es:",resta(leerEntero("Num1:"), leerEntero("Num2:")))
        # elif opcion == 3:
        #     print("La multiplicacion es:",multiplicacion(leerEntero("Num1:"), leerEntero("Num2:")))
        # elif opcion == 4:
        #     num1 = leerEntero("Num1:")
        #     num2 = validaCero(leerEntero("Num2:"))
        #     if (num2 != 0):
        #         print("La division es:",division(num1, num2))
        #     else:
        #         print("El divisor sigue siendo cero. Regresando al menu.")
        # elif opcion == 0:
        #     print("Chau ...")
        # else:        #     print("Opcion inválida")
