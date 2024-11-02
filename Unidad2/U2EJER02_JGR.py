import requests

'''
API DE BÚSQUEDA DE TRAGOS
Alumna: Jocelyn Gonzáles Ramírez 
Unidad 2. Ordinario
'''

while True: 
    print("Bienvenido a las recetas de cocteles:")
    print("Menú de bebidas:\n"
          "1. MARGARITA\n"
          "2. BLUE MARGARITA\n"
          "3. TOMMY'S MARGARITA\n"
          "4. WHITECAP MARGARITA\n"
          "5. SALIR\n")
    
    nombre_bebida = input("¿Qué bebida deseas buscar? (O escribe 'salir' para terminar): ").strip()
    
    if nombre_bebida.lower() == "salir":
        print("Adiós")
        break
    
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={nombre_bebida}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        
        if datos['drinks']:
            bebida_encontrada = datos['drinks'][0]  # Seleccionamos la primera coincidencia

            res = input("¿Qué quieres saber de la bebida?\n"
                        "a) Categoría\n"
                        "b) Ingredientes\n"
                        "c) Tipo de vaso\n"
                        "d) Instrucciones de preparación\n").strip().lower()

            if res == 'a':
                categoria = bebida_encontrada.get('strCategory', 'No disponible')
                print(f"Categoría: {categoria}")

            elif res == 'b':
                print(f"Ingredientes para '{nombre_bebida}':")
                for i in range(1, 16):  
                    ingrediente = bebida_encontrada.get(f'strIngredient{i}')
                    medida = bebida_encontrada.get(f'strMeasure{i}')
                    
                    if ingrediente:
                        if medida:
                            print(f"{ingrediente}: {medida.strip()}")
                        else:
                            print(f"{ingrediente}")
                            
            elif res == 'c':
                vaso = bebida_encontrada.get('strGlass', 'No disponible')
                print(f"Tipo de vaso: {vaso}")

            elif res == 'd':
                instrucciones = bebida_encontrada.get('strInstructions', 'No disponible')
                print(f"Instrucciones de preparación: {instrucciones}")

            else:
                print("Opción no válida.")
                
        else:
            print("No se encontró información sobre esa bebida.")
    else:
        print(" intenta de nuevo.")
