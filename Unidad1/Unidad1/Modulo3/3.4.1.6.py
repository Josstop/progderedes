'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 25 de septiembre del 2024
3.4.1.6 LABORATORIO: Lo básico de las listas
Descripción: Escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1).
Escribir una línea de código que elimine el último elemento de la lista (Paso 2).
Escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
'''
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: Solicitar al usuario un número y reemplazar el número central (índice 2).
nuevo_numero = int(input("Ingresa un número para reemplazar el número central: "))
hat_list[2] = nuevo_numero  # Reemplaza el número en la posición 2

# Paso 2: Eliminar el último elemento de la lista.
hat_list.pop()

# Paso 3: Imprimir la longitud de la lista existente.
print("La longitud de la lista es:", len(hat_list))

# Imprimir la lista final para ver el resultado
print(hat_list)
