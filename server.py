import socket
import threading

# Список для хранения всех сокетов клиентов
clients = []

# Функция для обработки сообщений от клиентов
def handle_client(client_socket, addr):
    while True:
        try:
            # Получаем сообщение от клиента
            message = client_socket.recv(1024).decode('utf-8')
            broadcast(message, client_socket)
        except ConnectionResetError:
            # Удаляем отключившегося клиента
            clients.remove(client_socket)
            print(f"Connection with {addr} has been closed")
            # Проверяем, остались ли еще подключенные клиенты
# Функция для отправки сообщения всем клиентам, кроме отправителя
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except ConnectionResetError:
                # Удаляем отключившегося клиента
                clients.remove(client)

# Запускаем сервер
def start_server():
    port = 5554
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(5)
    print(f"Server started. Waiting for connections on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection from {addr} has been established")
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

# Код для запуска сервера
start_server()

