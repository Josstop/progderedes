import requests

while True:
    print("C A T E G O R Í A S: \n animal"
    "career",
    "celebrity",
    "dev",
    "explicit",
    "fashion",
    "food",
    "history",
    "money",
    "movie",
    "music",
    "political",
    "religion",
    "science",
    "sport",
    "travel")
    categoria = input('Escribe salir para interrumpir la búsqueda\nIngresa la categoría de tu frase: ')
    if categoria == 'salir':
        print("ok Adiós")
        break
    url = f"https://api.chucknorris.io/jokes/random?category={categoria}"
    data =requests.get(url).json()
    frase = data['value']
    print("*****************************************************")
    print(str( frase))
    print("*****************************************************")
    while True:
        res = input('¿Quieres tener mas información de la frase?\nS / N')
        if res == "s":
            con = input('¿Que quieres saber?\na)Fecha de públicación\nb)Página oficial')
            if con == "a":
                fecha = data['created_at']
                print(fecha)
            elif con == "b":
                pag = data["url"]
                print(pag)
        elif res == "n":
            break
       
           