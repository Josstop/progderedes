'''
Autora: Jocelyn gonzáles Ramírez
Fecha: 30 dew septiembre del 2024
4.3.1.6 LABORATORIO: Un año bisiesto: escribiendo tus propias funciones
Descripción: Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve 
True si el año es un año bisiesto, o False si no lo es
'''
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Bisiesto
            else:
                return False  # No es bisiesto
        else:
            return True  # Bisiesto
    else:
        return False  # No es bisiesto

# Lista de años de prueba
test_data = [1900, 2000, 2016, 1987]

# Bucle para verificar cada año
for year in test_data:
    result = is_year_leap(year)  # Llama a la función para obtener el resultado
    print(f"{year} -> {result}") 