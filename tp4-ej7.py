"""
Ejercicio Nro 7
Escriba una función que utilice slicing para extraer 
las palabras que están en las posiciones pares de una frase. 
Por ejemplo, si se aplicara la función 
a la primera frase de este enunciado 
el resultado debería ser: 
['Escriba', 'función', 'utilice', 'para', 
'las', 'que', 'en', 'posiciones', 'de', 'frase'].
"""

# Función que devuelve las palabras en posiciones pares de una frase
def palabras_pares(frase: str) -> list:
    # Dividimos la frase en palabras, creando una lista
    palabras = frase.split()
    
    # Usamos slicing para obtener las palabras en índices pares
    # [::2] significa: desde el inicio hasta el final, de dos en dos
    resultado = palabras[::2]
    
    # Devolvemos la lista resultante
    return resultado

# Probamos la función 
frase_de_prueba = input("Ingrese una frase: ")

# Mostramos el resultado
print(palabras_pares(frase_de_prueba))
