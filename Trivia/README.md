# Trivia Numérica con Numbers API

¡Bienvenido al **Quiz de Trivia Numérica**!  
Este proyecto es un programa en Python que permite al usuario ingresar un número y obtener una curiosidad o dato interesante sobre él usando [Numbers API](http://numbersapi.com/).

El proyecto incluye:

- Función `trivia_fetch(num)` que obtiene trivia de Numbers API.
- Interacción en consola para jugar con el quiz.
- Manejo de errores para entradas inválidas o problemas de conexión.
- Compatible con pruebas automáticas (`test.py`) que verifican que la función devuelva el número correctamente.

## Uso

1. Ejecuta el programa principal:
```bash
python main.py
```

2. Ingresa un número cuando se te solicite.
3. Verás una trivia sobre ese número.
4. Escribe `salir` para terminar el programa.

Ejemplo de ejecución:

```
¡Bienvenido!
Para salir del programa escribe: salir
Ingresa un número: 5

Trivia sobre el número 5:
5 is the number of permanent members with veto power on the United Nations Security Council.
```

> Nota: Cada vez que ingreses el mismo número, la trivia puede cambiar, ya que Numbers API devuelve datos aleatorios para cada número.

---

## Pruebas automáticas

Para verificar que la función `trivia_fetch` cumple con los tests:

```bash
pytest test.py -q
```

Deberías ver que los tests pasan correctamente.

---

## Función principal

```python
def trivia_fetch(num: int) -> dict:
    # Llama a Numbers API y devuelve un diccionario con al menos la clave "number"
```
