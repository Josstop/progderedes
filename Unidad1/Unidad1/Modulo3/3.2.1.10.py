'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 25 de Septiembre del 2024
3.2.1.10 LABORATORIO: La sentencia continue - El Feo Devorador de Vocales
Descripción: Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.
'''
# Indicar al usuario que ingrese una palabra
# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra ingresada a mayúsculas
user_word = user_word.upper()

# Bucle for para recorrer cada letra de la palabra
for letter in user_word:
    # Condición para omitir las vocales
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue  # Omitir el bloque actual y pasar a la siguiente iteración
    # Imprimir las letras no consumidas (no vocales)
    print(letter)
