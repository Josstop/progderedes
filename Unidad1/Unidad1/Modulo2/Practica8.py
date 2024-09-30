'''
Autora: Jocelyn Gonzáles Ramírez
Descripcion: La tarea es completar el código para evaluar y mostrar el resultado de cuatro operaciones aritméticas básicas.
El resultado debe ser mostrado en consola.
Quizá no podrás proteger el código de un usuario que intente dividir entre cero. Por ahora, no hay que preocuparse por ello.
2.6.1.9 LABORATORIO: Entradas y salidas simples

'''
a = float(input("Ingresa el primer número (a): ")) # ingresa un valor flotante para la variable a aquí
b = float(input("Ingresa el segundo número (b): ")) # ingresa un valor flotante para la variable b aquí

suma = a + b 
print(f"Resultado de la suma: {a} + {b} = {suma}") # muestra el resultado de la suma aquí 

resta = a - b
print(f"Resultado de la resta: {a} - {b} = {resta}")# muestra el resultado de la resta aquí

multiplicacion = a * b
print(f"Resultado de la multiplicación: {a} * {b} = {multiplicacion}") # muestra el resultado de la multiplicación aquí

if b != 0:  # Verifica si el denominador no es cero para evitar un error de división por cero
    division = a / b
    print(f"Resultado de la división: {a} / {b} = {division}")
else:
    print("Error: División por cero no permitida") # muestra el resultado de la división aquí

print("\n¡Eso es todo, amigos!")
