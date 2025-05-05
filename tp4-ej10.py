"""
Ejercicio Nro 10
Escribir un programa que cree una lista de tuplas simulando una canasto de compra. 
El programa debe preguntar el artículo y su precio y añadir el par a la tupla, 
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el costo total, 
con el siguiente formato usando alienación de f-strings.
Lista de la compra
Artículo 1      Precio
Artículo 2      Precio
Artículo 3      Precio
...             ...

Total           Costo
"""
lista_productos = []
total = 0

decide = 's'

while decide == 's':
    
    articulo = input("Ing. articulo: ")
    precio = float(input("Ing. precio: "))
    producto = (articulo, precio)
    lista_productos.append(producto)
    total += producto[1]

    decide = input("Desea agregar otro producto: (S/N): ").lower()

for i in range(len(lista_productos)):
    print(f"Articulo {i+1}: {lista_productos[i][0]} - Precio: {lista_productos[i][1]}")

print(f"Total de la compra: {total}")