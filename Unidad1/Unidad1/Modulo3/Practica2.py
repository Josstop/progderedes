'''
Autora:Jocelyn Gonzáles Ramírez
Fecha: 24 de septiembre del 2024
3.1.1.10 LABORATORIO: Operadores de comparación y ejecución condicional
Descripción: Cada vez que recibe una entrada en forma de la palabra Espatifilo, 
grita involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"

'''
palabra = input("Introduce tu palabra: ")  #Se pide la palabra

if palabra == "ESPATIFILIO": #Se establece la condición que se requiere
    print("¡Sí, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!") # Respuesta de que la condición se cumplio
elif palabra == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!") #Segunda opcion de la condición
else:
    print("¡ESPATIFILIO!, ¡No " + palabra + "!")  #Si la palbra no es ibgual a ninguna de la anteriores se realiza lo siguiente.