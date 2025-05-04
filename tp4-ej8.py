"""
Ejercicio Nro 8
Crea una tupla con los meses del año, luego pide números al usuario, 
si el numero esta entre 1 y la longitud máxima de la tupla, 
muestra el contenido de esa posición sino muestra un mensaje de error.
"""

meses = ("Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic")


while True:
    numero = int(input(f"Ingrese un numero (1-{len(meses)}): "))

    if numero>= 1 and numero <= len(meses):
        print(f"Numero ingresado corresponde a: {meses[numero-1]}")
    else:
        print(f"Error ! fuera de rango: {numero}")
        break
