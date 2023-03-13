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

def leerEntero(mensaje):
    contador = 0
    while contador < 3:
        try:
            entrada = int(input(mensaje))
            return entrada
        except ValueError:
            print("Error: debe ingresar un número entero.")
            contador += 1
    print("Se superó el número máximo de intentos fallidos.")
    return None

def leerConjunto():
    conj = []
    numElementos = leerEntero("Ingrese el número de elementos: ")
    if numElementos is None:
        return None

    for i in range(numElementos):
        while True:
            elem = leerEntero(f"Ingrese el elemento {i + 1}: ")
            if elem is None:
                return None
            elif elem not in conj:
                conj.append(elem)
                break
            else:
                print('El número ya existe en el conjunto.')

    return conj


def menuPrincipal():
    print("********* Operaciones con conjuntos  *********")
    print(" 0- Salir")
    print(" 1- Union")
    print(" 2- Interseccion")
    print(" 3- Diferencia")
    print(" 4- Diferencia Simétrica")
    opcion = leerEntero("     >>> Ingrese una opcion: ")
    return opcion
def main():
    conj1 = leerConjunto()
    if conj1 is None:
        print("Error al leer el conjunto 1.")
        return
    conj2 = leerConjunto()
    if conj2 is None:
        print("Error al leer el conjunto 2.")
        return

    while True:
        opcion = menuPrincipal()
        match opcion:
            case 0:
                print("Adiós, vuelve pronto.")
            case 1:
                union = unir(conj1, conj2)
                print(f"La unión de los conjuntos es: {union}")
            case 2:
                inter = interseccion(conj1, conj2)
                print(f"La intersección de los conjuntos es: {inter}")
            case 3:
                difer = diferencia(conj1, conj2)
                print(f"La diferencia de los conjuntos es: {difer}")
            case 4:
                diferSim = diferenciaSimétrica(conj1, conj2)
                print(f"La diferencia simétrica de los conjuntos es: {diferSim}")
            case _:
                print("Error: opción inválida.")
main()