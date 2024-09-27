'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 25 de Septiembre del 2024
3.2.1.14 LABORATORIO: Fundamentos del bucle while
Descripción: Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
y generar la altura de la pirámide que se puede construir utilizando estos bloques.
'''
# Solicitar al usuario que ingrese el número de bloques
blocks = int(input("Ingresa el número de bloques: "))
height = 0
current_layer_blocks = 1

# Mientras tengamos suficientes bloques para construir otra capa
while blocks >= current_layer_blocks:
    # Restar los bloques usados en la capa actual
    blocks -= current_layer_blocks
    # Incrementar la altura
    height += 1
    # Pasar a la siguiente capa, que requiere más bloques
    current_layer_blocks += 1

# Imprimir la altura de la pirámide
print("La altura de la pirámide:", height)
