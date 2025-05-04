"""
Ejercicio Nro 9
Crea una tupla con números, 
pide un numero por teclado 
e indica cuantas veces se repite.
"""

# Paso 1: Pedimos al usuario que ingrese números separados por coma
entrada = input("Ingrese números separados por coma (ej: 1,2,3): ")

# Paso 2: Convertimos esa cadena en una lista de textos (strings)
# split(",") separa los elementos usando la coma como separador
lista_texto = entrada.split(",")

# Mostramos para entender cómo queda esa lista (opcional)
print(f"Lista en texto: {lista_texto}")

# Paso 3: Creamos una lista vacía para guardar los números convertidos
lista_numeros = []

# Paso 4: Recorremos cada elemento de la lista de texto
for elemento in lista_texto:
    # .strip() elimina los espacios en blanco al principio y al final
    limpio = elemento.strip()

    # Convertimos el texto a número entero
    numero = int(limpio)

    # Lo agregamos a la lista de números
    lista_numeros.append(numero)

# Paso 5: Mostramos la lista de números (ya convertida)
print(f"Lista de números enteros: {lista_numeros}")

# Paso 6: Convertimos la lista a una tupla
tupla_numeros = tuple(lista_numeros)

# Paso 7: Mostramos la tupla final (opcional)
print(f"Tupla generada: {tupla_numeros}")

# Paso 8: Pedimos al usuario un número para contar cuántas veces se repite
buscar = int(input("Ingrese un número para contar cuántas veces se repite: "))

# Paso 9: Usamos el método .count() para contar apariciones
cantidad = tupla_numeros.count(buscar)

# Paso 10: Mostramos el resultado
print(f"El número {buscar} se repite {cantidad} veces en la tupla.")

"""
mi_lista = [1, 2, 2, 3, 2]
mi_tupla = (1, 2, 2, 3, 2)

# Ambos funcionan igual
print(mi_lista.count(2))   # → 3
print(mi_tupla.count(2))   # → 3

# Cantidad total de elementos
print(len(mi_lista))       # → 5
print(len(mi_tupla))       # → 5
"""

"""
datos = [4, 7, 4, 1, 4, 9]

print(datos.count(4))  # Resultado: 3
print(datos.count(9))  # Resultado: 1
print(datos.count(2))  # Resultado: 0 (no aparece)

---

tupla = (5, 3, 5, 2, 5)
print(tupla.count(5))  # Resultado: 3

"""