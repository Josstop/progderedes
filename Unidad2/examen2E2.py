import requests

def consultar_equipo(nombre_equipo):
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={nombre_equipo}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error en la solicitud.")
        return
    datos = response.json()
    if datos['teams']:
        equipo = datos['teams'][0]
        print(f"\nNombre de la liga: {equipo.get('strLeague', 'Desconocido')}")
        print(f"Descripción: {equipo.get('strDescriptionES', 'No disponible')}")
        print(f"Nombre del estadio: {equipo.get('strStadium', 'Desconocido')}")
        print(f"Página oficial: {equipo.get('strWebsite', 'No disponible')}")
    else:
        print("No se encontró información sobre el equipo.")

def consultar_jugador(nombre_jugador):
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={nombre_jugador}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error en la solicitud.")
        return
    datos = response.json()
    if datos['player']:
        jugador = datos['player'][0]
        print(f"\nNombre completo: {jugador.get('strPlayer', 'Desconocido')}")
        print(f"Nacionalidad: {jugador.get('strNationality', 'Desconocido')}")
        print(f"Equipo: {jugador.get('strTeam', 'Desconocido')}")
        print(f"Lugar de nacimiento: {jugador.get('strBirthLocation', 'Desconocido')}")
        print(f"Cuenta de Facebook: {jugador.get('strFacebook', 'No disponible')}")
        print(f"Altura: {jugador.get('strHeight', 'No disponible')}")
        print(f"Peso: {jugador.get('strWeight', 'No disponible')}")
    else:
        print("No se encontró información sobre el jugador.")

def listar_ligas():
    url = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error en la solicitud.")
        return
    datos = response.json()
    if datos['leagues']:
        for liga in datos['leagues']:
            print(f"\nID de la liga: {liga.get('idLeague', 'Desconocido')}")
            print(f"Nombre de la liga: {liga.get('strLeague', 'Desconocido')}")
    else:
        print("No se encontraron ligas.")

def consultar_liga_por_id(id_liga):
    url = f"https://www.thesportsdb.com/api/v1/json/3/lookupleague.php?id={id_liga}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error en la solicitud.")
        return
    datos = response.json()
    if datos['leagues']:
        liga = datos['leagues'][0]
        print(f"\nNombre de la liga: {liga.get('strLeague', 'Desconocido')}")
        print(f"Deporte: {liga.get('strSport', 'Desconocido')}")
        print(f"País: {liga.get('strCountry', 'Desconocido')}")
    else:
        print("No se encontró información sobre la liga.")

# Código principal
while True:
    print("\n--- Menú de opciones ---")
    print("1. Consultar equipo por nombre")
    print("2. Consultar jugador por nombre")
    print("3. Consultar listado de ligas")
    print("4. Consultar liga por ID")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        nombre_equipo = input("Ingresa el nombre del equipo: ")
        consultar_equipo(nombre_equipo)
    elif opcion == "2":
        nombre_jugador = input("Ingresa el nombre del jugador: ")
        consultar_jugador(nombre_jugador)
    elif opcion == "3":
        listar_ligas()
    elif opcion == "4":
        id_liga = input("Ingresa el ID de la liga: ")
        consultar_liga_por_id(id_liga)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
