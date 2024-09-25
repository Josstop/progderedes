'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 23/09/2024
3.2.1.3 LABORATORIO: Lo esencial del bucle while - Adivina el número secreto
Descripción: Comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago.
 Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje 
 "¡Ja, ja! ¡Estás atrapado en mi bucle!"  y se le solicitará que ingrese un número nuevamente. Si el número ingresado 
 por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir 
 las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora".
'''
secret_number = 777 #Número declarado por el mago

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = int (input (":")) # se le solicita el número al usuario
while number != 0: # la condición es que si el numero es ditinto a cero se ejecute lo siguiente
    if number == secret_number:
        
            print ("¡Bien hecho, muggle! Eres libre ahora")
            break 
    else:
        print ("¡Ja, ja! ¡Estás atrapado en mi bucle!")
        number = int (input("Introduce nuevamente el numero:"))