import requests
#url = "https://jsonplaceholder.typicode.com/posts/8"
url = "http://127.0.0.1:5000/tasks"
response = requests.get(url)
if response.status_code == 200:
     data = response.json() 
     print('Solicitud Exitosa')
     print("Datos: ", data[3])
else:
    print("Error en la solicitud: ", response.text)
