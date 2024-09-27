'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 25 de Septiembre del 2024
3.2.1.15 LABORATORIO: Hipótesis de Collatz
Descripcion: Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. 
También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores 
intermedios de c0.
'''
# Solicitar al usuario que ingrese un número natural (mayor que 0)
c0 = int(input("Ingresa un número natural: "))

# Verificar si el número ingresado es válido
if c0 <= 0:
    print("El número debe ser un entero positivo.")
else:
    # Inicializar el contador de pasos
    pasos = 0

    # Ejecutar el bucle mientras c0 sea diferente de 1
    while c0 != 1:
        print(c0)  # Mostrar el valor actual de c0
        if c0 % 2 == 0:
            # Si c0 es par, dividirlo entre 2
            c0 = c0 // 2
        else:
            # Si c0 es impar, calcular 3 * c0 + 1
            c0 = 3 * c0 + 1
        pasos += 1  # Incrementar el contador de pasos

    print(c0)
    print("Se realizaron", pasos, "pasos.")