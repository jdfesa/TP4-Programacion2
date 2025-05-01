"""
Ejercicio Nro 4
Crea un programa que elija al azar elementos 
de una lista de 20  elementos generados al azar, 
usando la función choice. 
Debe mostrar 5 elementos aleatorios.
"""
import random

def generar_lista_aleatoria(cantidad: int, minimo: int, maximo: int) -> list:
    lista = []
    for _ in range(cantidad):
        numero = random.randint(minimo, maximo)
        lista.append(numero)
    return lista

def elegir_elementos_sin_repetir(lista: list, cantidad: int) -> list:
    elegidos = []
    while len(elegidos) < cantidad:
        elem = random.choice(lista)
        if elem not in elegidos:
            elegidos.append(elem)

    return elegidos

def main() -> None:
    lista = generar_lista_aleatoria(20, 1, 100)
    print("Lista generada: ")
    print(lista)

    elementos_elegidos = elegir_elementos_sin_repetir(lista, 5)
    print("\n5 elementos elegidos al azar (sin repetir): ")
    print(elementos_elegidos)

if __name__ == "__main__":
    main()
