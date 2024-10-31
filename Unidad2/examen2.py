##Alumna:Jocelyn
import requests

clave_api = "edf6678954a948b6a3386cbeb5e31a74"
url = "https://newsapi.org/v2/everything"

def obtener_noticias_por_autor(autor, fecha):
    parametros = {
        "q": autor,
        "from": fecha,
        "apiKey": clave_api
    }
    respuesta = requests.get(url, params=parametros)
    return respuesta

def obtener_noticias_por_fuente(fuente, fecha):
    parametros = {
        "domains": fuente,
        "from": fecha,
        "apiKey": clave_api
    }
    respuesta = requests.get(url, params=parametros)
    return respuesta

def listar_noticias(fecha):
    parametros = {
        "from": fecha,
        "apiKey": clave_api
    }
    respuesta = requests.get(url, params=parametros)
    return respuesta

fecha = "2024-10-23"
while True:
    print("\n--- Menú ---")
    print("1. Buscar noticias por autor")
    print("2. Buscar noticias por fuente de información")
    print("3. Listar noticias por autor y título")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        autor = input("Ingresa el nombre del autor: ").strip()
        if autor:
            respuesta = obtener_noticias_por_autor(autor, fecha)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                print(f"Código de estado: {respuesta.status_code}")
                print(f"Total de resultados: {datos['totalResults']}")
                for articulo in datos.get("articles", []):
                    print(f"Autor: {articulo.get('author')}")
                    print(f"Título: {articulo.get('title')}")
                    print(f"Descripción: {articulo.get('description')}")
                    print("-" * 40)
            else:
                print("Error en la consulta:", respuesta.status_code)
        else:
            print("El nombre del autor no puede estar vacío.")
    
    elif opcion == "2":
        fuente = input("Ingresa el nombre de la fuente (por ejemplo, gizmodo.com): ").strip()
        if fuente:
            respuesta = obtener_noticias_por_fuente(fuente, fecha)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                print(f"Código de estado: {respuesta.status_code}")
                print(f"Total de resultados: {datos['totalResults']}")
                for articulo in datos.get("articles", []):
                    print(f"Autor: {articulo.get('author')}")
                    print(f"Título: {articulo.get('title')}")
                    print(f"Descripción: {articulo.get('description')}")
                    print("-" * 40)
            else:
                print("Error en la consulta:", respuesta.status_code)
        else:
            print("La fuente de información no puede estar vacía.")
    
    elif opcion == "3":
        respuesta = listar_noticias(fecha)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            print(f"Código de estado: {respuesta.status_code}")
            print(f"Total de resultados: {datos['totalResults']}")
            for articulo in datos.get("articles", []):
                print(f"Autor: {articulo.get('author')}")
                print(f"Título: {articulo.get('title')}")
                print("-" * 40)
        else:
            print("Error en la consulta:", respuesta.status_code)
    
    elif opcion == "4":
        print("Adiós")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
