"""
Ejercicio Nro 1
Escribir un programa que almacene diferentes lenguajes
de programación (Python, Java, JavaScript, Haskell, 
Kotlin, 
C++, Ruby, Lua, PHP, 
Swift, SQL) en una lista 
y muestre por pantalla el siguiente mensaje: 
"Yo estudio, {nombre_del_lenguaje}" para todos estos.
"""

lista = ["Python", "Java", "JavaScript", "Haskell",
         "C++", "Ruby", "Lua", "PHP"]

"""
for i in lista:
    #Aqui se muestra el elemento directamente
    print(f"Yo estudio {i}") 
    # print(f"{lista[i]}") # NO hacer esto cuando uso in
"""

for i in range(len(lista)):
    #Aqui se muestra el elemento a traves del indice
    print(f"Yo estudio {lista[i]}")

