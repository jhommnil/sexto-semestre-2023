def leerEntero(mensaje):
    contador = 0
    while contador < 3:
        try:
            return int(input(mensaje))
        except:
            print(": Entero no válido..")
            contador = contador + 1
    print("Se superó el número máximo de intentos fallidos.")
    return leerConjunto()
def leerEnteroMenu(mensaje):
    contador = 0
    while contador < 3:
        try:
            return int(input(mensaje))
        except:
            print(": Entero no válido..")
            contador = contador + 1
    print("Se superó el número máximo de intentos fallidos.")
    return menuPrincipal()
def menuPrincipal():
    print("********* Operaciones con conjuntos  *********")
    print(" 0- Salir")
    print(" 1- Union")
    print(" 2- Interseccion")
    print(" 3- Diferencia")
    print(" 4- Diferencia Simétrica")
    return leerEnteroMenu("     >>> Ingrese una opcion: ")

def leerConjunto():
    conj = []
    numElementos = leerEntero("  Ingrese el numero de elementos: ")


    for i in range(numElementos):
        elem = leerEntero(f"  Ingrese el elemento {i+1}: ")
        if elem not in conj:
            conj.append(elem)
        else:
            print('El numero ya existe')
            return leerConjunto()
    return conj

def unir(conj1, conj2):
    union = []
    for elem in conj1:
        if elem not in union:
            union.append(elem)
    for elem in conj2:
        if elem not in union:
            union.append(elem)
    return union

def diferencia(conj1, conj2):
    difer = []
    for elem in conj1:
        if elem not in conj2:
            difer.append(elem)
    return difer

def diferenciaSimétrica(conj1, conj2):
    diferSim = unir(diferencia(conj1, conj2), diferencia(conj2, conj1))
    return diferSim

def interseccion(conj1, conj2):
    inter = []
    for elem in conj1:
        if elem in conj2 and elem not in inter:
            inter.append(elem)
    return inter

def main():
    conj1 = leerConjunto()
    conj2 = leerConjunto()
    while True:
        opcion = menuPrincipal()
        if opcion == 0:
            print(" Adios, vuelve pronto. ")
            break
        elif opcion == 1:
            union = unir(conj1, conj2)
            print(f" La union de los conjuntos es: {union}")
        elif opcion == 2:
            inter = interseccion(conj1, conj2)
            print(f" La interseccion de los conjuntos es: {inter}")
        elif opcion == 3:
            difer = diferencia(conj1, conj2)
            print(f" La diferencia de los conjuntos es: {difer}")
        elif opcion == 4:
            diferSim = diferenciaSimétrica(conj1, conj2)
            print(f" La diferencia simetrica de los conjuntos es: {diferSim}")
        else:
            print(" Error: opción inválida.")

main()