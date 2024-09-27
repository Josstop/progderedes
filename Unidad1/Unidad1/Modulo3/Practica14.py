'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 25 de septiembre del 2024
3.6.1.9 LABORATORIO: Operando con listas - conceptos básicos
Descripción: Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. 
El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.
'''
# Lista original con números repetidos
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Creamos una nueva lista donde solo se guardarán los elementos únicos
unique_list = []

# Recorremos la lista original
for num in my_list:
    # Si el número no está en unique_list, lo agregamos
    if num not in unique_list:
        unique_list.append(num)

# Imprimimos la lista con elementos únicos
print("La lista con elementos únicos:")
print(unique_list)
