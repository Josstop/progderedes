import requests
import json
import time
#Se utilizo una API de NASA Para devolver imágenes de diferentes cámaras
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY"

payload = {}
headers = {
    'Content-Type': 'application/json',
    'x-api-key': 'Y0ZH5MkDIf019Q701rv9vGd2KNOBn9nPfRk7Fx1B'
}

while True:
    print("*************************************************************************")
    camera = input("Ingresa el nombre de la cámara \n - FHAZ \n - RHAZ \n - MAST \n  o 'salir' para finalizar: ")
    print("**************************************************************************")
    if camera.lower() == 'salir' or camera.lower() == 's': 
        break 
    request_url = f"{url}&camera={camera.upper()}"
    print(f"Solicitando imágenes desde: {request_url}")

    response = requests.get(request_url)
    if response.status_code == 200:
        json_data = response.json() 
        photos = json_data.get('photos', [])

        if photos:  
            print(f"Se encontraron {len(photos)} imágenes para la cámara {camera.upper()}:")
            for idx, photo in enumerate(photos[:5], 1):  #  solo las primeras 5 imágenes
                print(f"{idx}. {photo['img_src']}")
        else:
            print(f"No se encontraron imágenes para la cámara {camera.upper()}.")
    elif response.status_code == 401:
        print("Usuario no autorizado. Verifique la clave API.")
    else:
        print(f"Error: código {response.status_code}, no se pudo obtener las imágenes.")
    time.sleep(3)

print("Adiós POPO")
