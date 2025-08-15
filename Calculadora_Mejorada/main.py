# Función para sumar todos los números de una lista
def addmultiplenumbers(list):
    # Si la lista está vacía regresa 0 para evitar errores.
    if not list:
        return 0
    total = 0

    # Se hace el recorrido de cada número de la lista
    for n in list:
        # Se hace la suma de cada número
        total = total + n
    # Regresamos el valor de la suma
    return total


# Función para multiplicar todos los números de una lista
def multiplymultiplenumbers(lista):
    # Si la lista está vacía regresamos 1
    if not lista:
        return 1
    total = 1

    # Se hace el recorrido de cada número de la lista
    for n in lista:
        # Multiplicamos el total por cada número de la lista
        total = total * n
        # Regresamos el valor de la multiplicación
    return total


# Función para revisar si un número es entero
def isitaninteger(numero):
    # Hacemos uso del módulo 1 y si el residuo es 0 el numero evaluado es entero
    if numero % 1 == 0:
        # Regresamos un True
        return True
    # Regresamos un False
    else:
        return False


# Función para saber si un número es par y entero
def isiteven(numero):
    # Si el número no es entero regresamos un False
    if numero % 1 != 0:
        return False

    # Una vez que sabemos que es entero comprobamos si es par
    if numero % 2 == 0:
        # Si es par regresamos True
        return True
    # Si no es par regresamos un False
    else:
        return False


def main():
    print("¡Bienvenido a la calculadora mejorada!")

    # Bucle infinito para que el menú se repita hasta salir
    while True:  
        # Mostramos las opciones del menú
        print("\nElige una opción:")
        print("1. Sumar una lista de números")
        print("2. Multiplicar una lista de números")
        print("3. Ver si un número es par")
        print("4. Ver si un número es entero")
        print("5. Salir")

        # Preguntamos al usuario que desea realizar
        opcion = input("Ingresa tu opción (1-5): ")  

        # Opción 1: Sumar los números de una lista
        if opcion == "1":
            entrada = input("Ingresa los números separados por comas: ")
            # Convertimos la entrada a una lista de números (float)
            lista = [float(x) for x in entrada.split(",")]
            resultado = addmultiplenumbers(lista)  # Llamamos a la función
            print("Resultado de la suma:", resultado)

        # Opción 2: Multiplicar los números de una lista
        elif opcion == "2":
            entrada = input("Ingresa los números separados por comas: ")
            lista = [float(x) for x in entrada.split(",")]
            resultado = multiplymultiplenumbers(lista)
            print("Resultado de la multiplicación:", resultado)

        # Opción 3: Verificar si un número es par
        elif opcion == "3":
            numero = float(input("Ingresa un número: "))
            if isiteven(numero):
                print(f"{numero} es par.")
            else:
                print(f"{numero} no es par.")

        # Opción 4: Ver si un número es entero
        elif opcion == "4":
            numero = float(input("Ingresa un número: "))
            if isitaninteger(numero):
                print(f"{numero} es un número entero.")
            else:
                print(f"{numero} no es un número entero.")

        # Opción 5: Salir
        elif opcion == "5":
            print("¡Gracias por usar la calculadora!")
            # Salimos del bucle y terminamos el programa
            break  

        # Opción inválida
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
