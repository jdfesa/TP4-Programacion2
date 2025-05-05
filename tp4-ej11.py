"""
Ejercicio Nro 11
Escribe un programa para generar contraseñas. 
Entre las generadas evaluaremos las siguientes características:
•     Longitud fija de 12 caracteres
•     No pueden tener letras consecutivas (sT es tan inválido como ST o St)
•     No puede tener un número antes o después de una vocal
•     Si tiene un _ debe tener un dígito después de este a menos que sea el último carácter
Luego, genere una lista de 20 contraseñas que solo estén obligadas a cumplir la longitud.  
Con  estas,  imprima  una  tabla  en  donde  la  primera  columna  es  la contraseña 
y la segunda es Sí/No controlando la validez de las características mencionadas anteriormente.
"""
from random import choice
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, punctuation

def longitud_12_caracteres(contrasena: str) -> bool:
    return len(contrasena) == 12

def validar_letras_consecutivas(contrasena: str) -> bool:
    # Recorre la contraseña y busca si hay dos letras seguidas
    for i in range(len(contrasena) - 1):
        if contrasena[i].isalpha() and contrasena[i + 1].isalpha():
            return False  # Hay letras seguidas → inválida
    return True  # No hay letras seguidas → válida

def validar_numeros_antes_despues_vocal(contrasena: str) -> bool:
    vocales = "aeiouAEIOU"
    for i in range(len(contrasena) - 1):
        actual = contrasena[i]
        siguiente = contrasena[i + 1]

        #Vocal seguida de número
        if actual in vocales and siguiente.isdigit():
            return False

        #Número seguido de vocal
        if actual.isdigit() and siguiente in vocales:
            return False
    return True

def valida_guion_bajo_antes_de_numero(contrasena: str) -> bool:
    # Recorremos cada posición de la contraseña
    for i in range(len(contrasena)):
        
        # Si encontramos un guion bajo en la posición actual
        if contrasena[i] == "_":
            
            # Caso 1: el guion bajo está al final de la cadena
            if i == len(contrasena) - 1:
                # Es válido, así que simplemente seguimos con el siguiente carácter
                continue  # Salta al próximo ciclo del for (no evalúa lo que sigue)
            
            # Caso 2: el carácter siguiente NO es un número
            elif not contrasena[i + 1].isdigit():
                # No cumple la regla, por lo tanto la contraseña es inválida
                return False
    
    # Si revisamos toda la contraseña y no hubo errores, entonces es válida
    return True

def generacion_contrasena() -> str:
    caracteres = ascii_letters + digits + punctuation
    longitud = 12

    contrasena = []
    for _ in range(longitud):
        letra = choice(caracteres)
        contrasena.append(letra)

    return ''.join(contrasena)  # Convertir lista a string

def validacion_contrasena(contrasena: str) -> bool:
    return (
        longitud_12_caracteres(contrasena)
        and validar_letras_consecutivas(contrasena)
        and validar_numeros_antes_despues_vocal(contrasena)
        and valida_guion_bajo_antes_de_numero(contrasena)
    )

def main() -> None:
    lista_de_contrasenas = []

    for _ in range(20):
        lista_de_contrasenas.append(generacion_contrasena())

    print(f"{'Contraseña':<20} {'¿Válida?'}")
    print("-" * 30)

    for contrasena in lista_de_contrasenas:
        if validacion_contrasena(contrasena):
            print(f"{contrasena:<20} Sí")
        else:
            print(f"{contrasena:<20} No")

if __name__ == "__main__":
    main()
