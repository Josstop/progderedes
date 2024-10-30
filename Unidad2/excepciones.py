try: #Tiene vigilado todo el código por cualquier error
    num = int(input("Ingresa tu edad"))
    res = 1/num
    print(num)

  
except Exception:
    print("Hubo ubn error")
finally:
    print("Si no sucede de todas maneras me ejecuto")