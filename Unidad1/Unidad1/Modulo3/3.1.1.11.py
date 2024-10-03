'''
Autora: Jocelyn Gonzáles Ramírez
3.1.1.11 LABORATORIO: Fundamentos de la sentencia if-else
Fecha: 24/09/2024
Descripción: Escribir una calculadora de impuestos.
Debe aceptar un valor de punto flotante: el ingreso.
A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. 
Hay una función llamada round() que hará el redondeo por ti, la encontrarás en el 
código de esqueleto del editor.
'''
income = float(input("Introduce el ingreso anual:")) #Se pide el ingreso anual

if income <85528: # Se realiza el analisis del ingreso y se ejecuta segun la condición
    tax = ((income*18)/100) - 556.2
else:
    tax = 14839.2 + (((income - 85528) * 32)/100)
tax = round(tax, 0)
if tax < 0: # Se verifica que si el tax es menor a 0 no hay impuestos
    tax = 0.0
print("El impuesto es:", tax, "pesos")
