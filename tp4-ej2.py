"""
Ejercicio Nro 2
Escribir un programa que almacene las asignaturas 
de un curso (Matemáticas, Física, Química, 
Historia y Lengua) en una lista, 
pregunte al usuario la nota que 
ha  sacado  en  cada  asignatura.  
Mostrar  por  pantalla  la  nota  
y  asignatura correspondiente.
"""
materias = ["Matematicas", "Fisica", "Quimica", "Historia",
            "Lengua"]
notas = []
for i in materias:
    print(f"{i}")
    notas.append(int(input("Ingrese nota correspondiente: ")))

for i in range(len(materias)):
    print(f"{materias[i]}: {notas[i]}")