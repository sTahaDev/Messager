import socket


class Messager:
    def __init__(self) -> None:
        self.file_data = ""
        pass

    def read(self, data):
        data = data.split(" ")

        if data[0] == "msg":
            return data[0]

        elif data[0] == "file":
            file_path = data[1]

            with open(file_path, "r") as file:
                file_data = file.read()

            return ("file " + file_path, file_data.encode("utf-8"))

        elif data[0] == "image":
            file_path = data[1]

            with open(file_path, "rb") as file:
                file_data = file.read()

            return ("image " + file_path, file_data)

        return ("Fail", "Fail!")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("raspberry_pi_ip_adress", 1234)

client_socket.connect(server_address)

messager = Messager()

while True:

    message = input("Messager: ")

    if message.lower() == "exit":
        break

    type, message = messager.read(message)

    client_socket.send(type.encode("utf-8"))
    client_socket.recv(1024)  # Sunucunun "Stage2" mesajını al
    client_socket.send(message)

client_socket.close()
