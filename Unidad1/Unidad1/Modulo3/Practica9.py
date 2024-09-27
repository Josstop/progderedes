'''
Autora:Jocleyn Gonzáles Ramírez
Fecha: 25 de septiembre del 2024
3.2.1.11 LABORATORIO: La sentencia continue - El Bonito Devorador de Vocales
Descripción:  ¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior (3.1.2.10) y crear un mejor 
devorador de vocales (bonito) mejorado!
Escribe un programa que use:
Un bucle for.
El concepto de ejecución condicional (if-elif-else).
La instrucción continue.
'''
# Crear una variable para almacenar la palabra sin vocales
word_without_vowels = ""

# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

# Bucle for para recorrer cada letra de la palabra
for letter in user_word:
    # Si la letra es una vocal, la omitimos usando continue
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    # Si la letra no es una vocal, la agregamos a la variable word_without_vowels
    word_without_vowels += letter

# Imprimir la palabra sin vocales
print("Palabra sin vocales:", word_without_vowels)
