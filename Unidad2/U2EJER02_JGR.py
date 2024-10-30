import requests
'''
API DE BÚSQUEDA DE TRAGOS
Alumna: Jocelyn Gonzáles Ramírez 
Unidad 2. Ordinario

'''
while True: 
   # url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    print("Bienvenido a las recetas de cocteles:")
    #print("Menú de bebidas: "
    #     "1. M A R G A R I T A"
    #     "2. BLUE MARGARITA"
    #      "3. TOMMYS MARGARITA"
    #      "4. Whitecap Margarita"
    #      "2. BLUE MARGARITA"
    #       
    #     )
    #data =requests.get(url).json()
    nombreBebida= input("¿Que bebida deseas buscar?")
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={nombreBebida}"
    bebida = requests.get(url)
    if nombreBebida == 200:
       # if nombreBebida ==  "Margarita":
        datos = bebida.json()
        if datos["drinks"]:
            for bebida in datos["drinks"]:
                # Mostramos el nombre de la bebida
                print("Nombre de la bebida:", bebida["strDrink"])
                # Opcionalmente, mostramos otros detalles
                print("Categoría:", bebida["strCategory"])
                print("Tipo de vaso:", bebida["strGlass"])
                print("Instrucciones:", bebida["strInstructions"])
                print("Ingredientes:")
    else:
        print("Esa bebida no se encuentra")
