# Calculadora básica en Python

def calcular(iNum1, sOpe, iNum2):
    # Utilizamos la estructura "match" para comparar la entrada de la operación
    match sOpe:
        case "+":
            iRes = iNum1 + iNum2
        case "-":
            iRes = iNum1 - iNum2
        case "*":
            iRes = iNum1 * iNum2
        case "/":
            if iNum2!=0:
                iRes = iNum1 / iNum2
            else: 
                iRes='Error: División por cero'
        case "%":
            if iNum2!=0:
                iRes = iNum1 % iNum2
            else: 
                iRes='Error: Modulo por cero'
        case _:
                iRes = "Operación no válida"
# Imprimimos el resultado de la operación
    print(f"{iNum1}{sOpe}{iNum2}= {iRes}")


# Pedimos los números que estaran en las variables iNum1 e iNum2 y convertimos los string en int
iNum1 = int(input("Introduce un número: "))
sOpe = input("¿Que operación quieres hacer? (+ - * / %): ")
iNum2 = int(input("Introduce otro número: "))

calcular(iNum1, sOpe, iNum2)

# Menú para operaciones adicionales
while True:
    print("\n¿Quieres hacer otra operación?")
    print("1. Otra operación con 2 números")
    print("2. Operación con 3 números o más (ej: 2 + 4 - 3 * 2)")
    print("3. Salir")

    iOpc = input("Elige una opción: (1/2/3): ")

    if iOpc == "1":
        iNum1 = int(input("Introduce un número: "))
        sOpe = input("¿Qué operación quieres hacer? (+ - * / %): ")
        iNum2 = int(input("Introduce otro número: "))

        calcular(iNum1, sOpe, iNum2)

    elif iOpc == "2":
        expr = input("Introduce la operación (ej: 2 + 3 * 4 - 1): ")
        try:
            res = eval(expr)
            print(f"{expr} = {res}")
        except Exception as e:
            print("Error en la expresión:", e)

    elif iOpc == "3":
        print("¡Gracias por usar la calculadora!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")