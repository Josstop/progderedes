##Alumna:Jocelyn
import requests

def linea(simbolo="=", longitud=40):
    print(simbolo * longitud)

def buscar_libro(titulo):
    url = "https://openlibrary.org/search.json"
    params = {"q": titulo}
    respuesta = requests.get(url, params=params)
    if respuesta.status_code != 200:
        print("Error en la solicitud")
        return None
    return respuesta.json()

while True:
    titulo = input("Ingresa el título del libro que deseas buscar: ").strip()
    if titulo:
        break
    else:
        print("Por favor, ingresa un título válido.")

datos = buscar_libro(titulo)

if datos and 'docs' in datos:
    print(f"\nResultados encontrados para '{titulo}':")
    linea()

    for libro in datos['docs']:
        titulo_libro = libro.get("title", "Título desconocido")
        autores = libro.get("author_name", ["Autor desconocido"])
        ano_publicacion = libro.get("first_publish_year", "Año desconocido")
        url_mas_info = f"https://openlibrary.org{libro.get('key', '')}"

        print(f"Título: {titulo_libro}")
        print(f"Autor(es): {', '.join(autores)}")
        print(f"Año de publicación: {ano_publicacion}")
        print(f"Más información: {url_mas_info}")
        linea()
else:
    print("No se encontraron resultados para el título ingresado.")
