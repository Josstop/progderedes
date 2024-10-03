'''
Autora: Jocelyn Gonzáles Ramírez
Fecha 1 de Ostubre del 2024
4.3.1.8 LABORATORIO: Día del año: escribiendo y utilizando tus propias funciones

'''
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
