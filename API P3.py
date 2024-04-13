import requests
url = "https://api.jikan.moe/v4/top/anime"
try:
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        for e in data["data"]:
            print("Anime:", e["title"])
            print("Tipo:", e["type"])
            print("URL:", e["url"])
    else:  
     print("Error al consultar API. Por favor, inténtalo de nuevo más tarde.")
except requests.exceptions.RequestException:
    print("Error al realizar la solicitud. Por favor, asegúrate de tener una conexión a Internet.")