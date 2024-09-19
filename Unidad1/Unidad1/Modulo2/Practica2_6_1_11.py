'''
Practica de laboratorio: Operadores 

'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos):"))
dura = int(input("Duración del eventp (minutos): "))

total = mins + dura
cociente = total // 60
residuo = total % 60
hour += cociente

print(f"{hour}: {residuo}")
