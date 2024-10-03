'''
Autora: Jocelyn Gonzáles Ramírez
4.3.1.7 LABORATORIO: ¿Cuántos días?: escribiendo y utilizando tus propias funciones
Descripción: 
'''
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Año bisiesto
            else:
                return False  # No es bisiesto
        else:
            return True  # Año bisiesto
    else:
        return False  # No es bisiesto

def days_in_month(year, month):
    # Si el mes no es válido, devolver None
    if month < 1 or month > 12:
        return None
    
    # Lista con los días de cada mes
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Si es febrero y el año es bisiesto, devolver 29 días
    if month == 2 and is_year_leap(year):
        return 29
    
    # Devolver los días correspondientes al mes
    return days_in_month_list[month - 1]

# Pruebas
test_years = [1900, 2000, 2016, 1987, 2023, 2024, 1800]
test_months = [2, 2, 1, 11, 4, 2, 2]
test_results = [28, 29, 31, 30, 30, 29, 28]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(f"{yr}, {mo} -> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print(f"Fallido (Resultado: {result}, Esperado: {test_results[i]})")