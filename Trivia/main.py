import requests


def trivia_fetch(num: int) -> dict:
    url = f"http://numbersapi.com/{num}?json"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
    except Exception:
        data = {"number": num, "text": "No se pudo obtener la trivia."}
    return data


def main():
    print("¡Bienvenido!")
    print("Para salir del programa escribe: salir")

    while True:
        entrada = input("Ingresa un número: ").strip()
        if entrada.lower() == "salir":
            print("Gracias por usar el programa")
            break
        try:
            numero: int = int(entrada)
            trivia = trivia_fetch(numero)
            print(f"\nTrivia sobre el número {numero}:")
            print(f"  {trivia.get('text', 'No hay información disponible.')}\n")
        except ValueError:
            print("Por favor, ingresa un número válido.\n")


if __name__ == "__main__":
    main()
