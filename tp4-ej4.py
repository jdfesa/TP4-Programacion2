"""
Ejercicio Nro 4
Crea un programa que elija al azar elementos 
de una lista de 20  elementos generados al azar, 
usando la función choice. 
Debe mostrar 5 elementos aleatorios.
"""

# Importamos solo las funciones necesarias del módulo random
from random import randint, choice

def generar_lista_aleatoria(cantidad: int, minimo: int, maximo: int) -> list:
    lista = []

    # Repetimos la cantidad de veces que nos pidan
    for _ in range(cantidad):

        # Generamos un número aleatorio entre mínimo y máximo
        numero = randint(minimo, maximo)

        # Lo agregamos a la lista
        lista.append(numero)

    return lista

# Función que elige elementos al azar sin repetirlos
def elegir_elementos_sin_repetir(lista: list, cantidad: int) -> list:
    elegidos = []

    # Mientras no tengamos la cantidad deseada
    while len(elegidos) < cantidad:

        # Elegimos un elemento al azar de la lista original
        elem = choice(lista)

        # Si ese elemento todavía no fue elegido, lo agregamos
        if elem not in elegidos:
            elegidos.append(elem)

    return elegidos

def main() -> None:

    # Generamos una lista de 20 números aleatorios entre 1 y 100
    lista = generar_lista_aleatoria(20, 1, 100)
    
    print("Lista generada: ")
    print(lista)

    elementos_elegidos = elegir_elementos_sin_repetir(lista, 5)
    print("\n5 elementos elegidos al azar (sin repetir): ")
    print(elementos_elegidos)

if __name__ == "__main__":
    main()
