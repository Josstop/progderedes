'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 25 de septiembre del 2024
3.4.1.13 LABORATORIO: Lo básico de las listas - Los Beatles
Descripción: Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. 
'''
# Paso 1: Crear una lista vacía llamada 'beatles'
beatles = []
print("Paso 1:", beatles)

# Paso 2: Agregar a John Lennon, Paul McCartney y George Harrison usando append()
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# Paso 3: Usar un bucle para agregar a Stu Sutcliffe y Pete Best
for miembro in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(miembro)
print("Paso 3:", beatles)

# Paso 4: Eliminar a Stu Sutcliffe y Pete Best de la lista
del beatles[4]  # Eliminar a Pete Best
del beatles[3]  # Eliminar a Stu Sutcliffe
print("Paso 4:", beatles)

# Paso 5: Agregar a Ringo Starr al principio usando insert()
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

# Verificar la longitud de la lista final
print("Los Beatles finales son:", beatles)
print("La longitud de la lista es:", len(beatles))
