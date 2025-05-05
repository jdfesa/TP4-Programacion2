"""
Ejercicio Nro 12
En el juego clásico de piedra-papel-tijera tenemos las siguientes reglas:
•     Piedra gana a Tijera
•     Tijera gana a Papel
•     Papel gana a Piedra
Ahora agregaremos reglas especiales al juego:
•     Si se ganó con piedra se invierten todas las reglas
        -> Piedra gana a Papel
        -> Tijera gana a Piedra
        -> Papel gana a Tijera

•     Si se empató con cualquiera se restauran las reglas originales
Cree un programa que simule 10 partidas de este juego y los eventos registrados, 
cambio de reglas, victorias, empates. 
Luego muestre una tabla con número del 
movimiento y el tipo de evento registrado. 
El evento de fin de juego se registra luego del evento del último jugador.
"""

"""piedra = 1
tijera = 2
papel = 3


1      vs 2 = 1
piedra vs tijera = 1
piedra vs papel = 3
piedra vs piedra = 1

tijera vs piedra = 1
tijera vs papel = 2
tijera vs tijera = 2

3 vs 2 = 2
papel vs tijera = 2
papel vs piedra = 3
papel vs papel = 3"""

from random import choice

# Definimos los movimientos
PIEDRA = 1
TIJERA = 2
PAPEL = 3
MOVIMIENTOS = [PIEDRA, TIJERA, PAPEL]
NOMBRES = {1: "Piedra", 2: "Tijera", 3: "Papel"}

# Reglas originales
def reglas_originales() -> dict:
    return {
        PIEDRA: TIJERA,   # Piedra gana a Tijera
        TIJERA: PAPEL,    # Tijera gana a Papel
        PAPEL: PIEDRA     # Papel gana a Piedra
    }

# Reglas invertidas
def reglas_invertidas() -> dict:
    return {
        PIEDRA: PAPEL,    # Piedra gana a Papel
        TIJERA: PIEDRA,   # Tijera gana a Piedra
        PAPEL: TIJERA     # Papel gana a Tijera
    }

# Simula una ronda y determina el resultado
def jugar_ronda(j1: int, j2: int, reglas: dict) -> int:
    if j1 == j2:
        return 0  # Empate
    elif reglas[j1] == j2:
        return 1  # Gana jugador 1
    else:
        return 2  # Gana jugador 2

# Simula el juego completo
def simular_juego(n: int = 10):
    reglas = reglas_originales()
    eventos = []

    for ronda in range(1, n + 1):
        j1 = choice(MOVIMIENTOS)
        j2 = choice(MOVIMIENTOS)
        resultado = jugar_ronda(j1, j2, reglas)

        eventos.append(f"Ronda {ronda}: Jugador 1 eligió {NOMBRES[j1]}, Jugador 2 eligió {NOMBRES[j2]}")

        if resultado == 0:
            eventos.append("→ Empate: se restauran las reglas originales")
            reglas = reglas_originales()
        elif resultado == 1:
            eventos.append("→ Gana Jugador 1")
            if j1 == PIEDRA:
                eventos.append("→ Victoria con piedra: se invierten las reglas")
                reglas = reglas_invertidas()
        elif resultado == 2:
            eventos.append("→ Gana Jugador 2")

    eventos.append("→ Fin del juego")

    return eventos

# Función principal que muestra la tabla de eventos
def main():
    eventos = simular_juego(10)

    print(f"{'Movimiento':<50} Evento")
    print("-" * 70)
    for evento in eventos:
        print(f"{evento}")

if __name__ == "__main__":
    main()
