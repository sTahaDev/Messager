import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1234

server_socket.bind((host, port))

server_socket.listen(5)

print("Sunucu başlatıldı. İstemci bekleniyor...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} adresinden bağlantı kabul edildi.")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        data = data.decode().split(" ")
        file_name = data[1]

        # İstemciden gelen mesajı doğru bir şekilde işlemek için bir döngü oluşturuyoruz
        if data[0] == "file":
            client_socket.send("Stage2".encode("utf-8"))
            data = client_socket.recv(1024).decode()
            with open(file_name, "w") as file:
                file.write(data)
        elif data[0] == "image":
            client_socket.send("Stage2".encode("utf-8"))
            with open(file_name, "wb") as file:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    file.write(data)
        else:
            print(data)

    client_socket.close()
