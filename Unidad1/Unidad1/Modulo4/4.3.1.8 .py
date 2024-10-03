'''
Autora: Jocelyn Gonzáles Ramírez
fecha: 01 de octubre del 2024
4.3.1.8 LABORATORIO: Día del año: escribiendo y utilizando tus propias funciones
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

def days_in_month(year, month):
 
    if month < 1 or month > 12:
        return None
    
  
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
  
    if month == 2 and is_year_leap(year):
        return 29
    
    return days_in_month_list[month - 1]

def day_of_year(year, month, day):
   
    days = days_in_month(year, month)
    if days is None or day < 1 or day > days:
        return None

    # Calcular el día correspondiente del año
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    total_days += day

    return total_days

# Pruebas
print(day_of_year(2000, 12, 31))  # Debería devolver 366 (año bisiesto)
print(day_of_year(2023, 3, 15))   # Debería devolver 74
print(day_of_year(2024, 2, 29))   # Debería devolver 60 (año bisiesto)
print(day_of_year(2024, 4, 31))   # Debería devolver None (abril no tiene 31 días)
print(day_of_year(1800, 2, 29))   # Debería devolver None (1800 no es bisiesto)
