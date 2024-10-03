'''
Alumna: Jocelyn Gonzáles Ramírez 
Fecha: 25 de Septiembre de 2024
3.2.1.9 LABORATORIO: La sentencia break - Atascado en un bucle
Descripción: Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que 
ingrese "chupacabra" como la palabra de salida secreta, en cuyo caso el mensaje "¡Has dejado el bucle con éxito". Debe imprimirse 
en la pantalla y el bucle debe terminar.
'''
palabra_secret = "chupacabra" # Se declara la palbra secreta
palabra = str(input("Ingresan la palabra secreta:"))
while True: #Se utiliza un bucle hasta que la palabra ingresada coincida
    palabra = input("Ingresa la palabra secreta: ")
    if palabra == palabra_secret:
        print("¡Has dejado el bucle con éxito!")
        break #Rompe el bucle