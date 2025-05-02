"""
Ejercicio Nro 6
Escribir un programa que pida al usuario una palabra 
y muestre por pantalla si es un palíndromo. 
Utilizando slicing.
"""


palabra = input("Ingrese una palabra: ")

if palabra == palabra[::-1]:
    print("Es palindromo!")
else:
    print("No es palindromo!")
