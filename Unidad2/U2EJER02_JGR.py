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
    
    nombreBebida = input("¿Qué bebida deseas buscar? (O escribe 'salir' para terminar): ").strip()
    
    if nombreBebida.lower() == "salir":
        print("Gracias por usar el buscador de cocteles. ¡Hasta la próxima!")
        break
    
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={nombreBebida}"
    bebida = requests.get(url)
    
    if bebida.status_code == 200:
        datos = bebida.json()
        # Verificamos si hay datos para mostrar
        if datos['drinks']:
            #buscar = datos.json()
            res = input("Que quieres saber de la bebida:\na)Categoria\nb)Ingredientes\nc)Tipo de vaso\nd)Insrucciones de preparación")
            res.lower()
            if res == 'a':
              i = bebida
              for i in 'drinks':
                categoria = datos['drinks'][0]['strCategory']
                print(f"Categoria: {categoria}")


            #print("Receta encontrada:")
            #print(datos)  # O puedes acceder a datos específicos en `datos['drinks']`
            #while True:
            
        else:
            print("No se encontró información sobre esa bebida.")
    else:
        print("Error en la búsqueda de la bebida. Por favor, intenta de nuevo.")
