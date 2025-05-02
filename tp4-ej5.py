"""
Ejercicio Nro 5
Escribir un programa que almacene el abecedario en una lista, 
elimine de la lista las letras que ocupen posiciones 
múltiplos de 3 (en la lista original), 
y muestre por pantalla la lista resultante.
"""

# Importamos solo la constante ascii_lowercase del módulo string
from string import ascii_lowercase

# ascii_lowercase contiene el string 'abcdefghijklmnopqrstuvwxyz'
# Al convertirlo en lista, obtenemos todas las letras por separado
letras = list(ascii_lowercase)

# Mostramos la lista generada
print(letras)

letras_pos = []
for i in range(len(letras)):
    if i % 3 == 0:
        letras_pos.append(letras[i])

print("Lista resultante: \n")
print(letras_pos)