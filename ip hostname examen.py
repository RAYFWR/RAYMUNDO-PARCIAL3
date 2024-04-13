import socket
def ip_host():
    try:
        hostname = socket.gethostname()
        print(hostname)
        ip = socket.gethostbyname(hostname)
        print("Dirección IP:", ip)
    except Exception as e:
        print("Error al optener ip,host")
if __name__ == "__main__":
    ip_host()