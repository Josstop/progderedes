'''
Autora: Jocelyn Gonzáles Ramírez
Fecha: 02/10/24
4.3.1.10 LAB: Convirtiendo el consumo de combustible

'''
def liters_100km_to_miles_gallon(liters):
  
    miles = 100000 / 1609.344
    gallons = liters / 3.785411784
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    kilometers = miles * 1.609344
    liters = 3.785411784
    return (liters / kilometers) * 100

# Pruebas
print(liters_100km_to_miles_gallon(3.9))  # Salida esperada: 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # Salida esperada: 31.36194444444444
print(liters_100km_to_miles_gallon(10.))  # Salida esperada: 23.52145833333333

print(miles_gallon_to_liters_100km(60.3)) # Salida esperada: 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4)) # Salida esperada: 7.490910297239916
print(miles_gallon_to_liters_100km(23.5)) # Salida esperada: 10.009131205673757
