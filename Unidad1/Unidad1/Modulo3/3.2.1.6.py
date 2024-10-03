'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 23 de Septiembre
3.2.1.6 LABORATORIO: Fundamentos del bucle for: el conteo
Descripción:  escribe un programa que use un bucle for para 
"contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, 
el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"
'''
import time
number = 1


for number in range (1, 6):    # Escribe un bucle for que cuente hasta cinco.
    print ( number,"Mississipi" )
    time.sleep(1) #cuenta el tiempo entre cada mensaje
    number = number + 1 # a la variable number sse le suma 1

print ("Listos o no aqui voy!")