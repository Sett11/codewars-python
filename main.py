import socket

def socket_server():
    # Создаем TCP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к localhost и порту 1111
    server_socket.bind(('localhost', 1111))
    
    # Начинаем слушать входящие соединения (1 - максимальное количество ожидающих соединений)
    server_socket.listen(1)
    print("Server is listening on port 1111...")
    
    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        try:
            while True:
                # Получаем данные от клиента (максимум 1024 байта)
                data = client_socket.recv(1024).decode('utf-8').strip()
                
                if not data:
                    # Если данные пустые, соединение закрыто клиентом
                    break
                
                if data == "exit":
                    # Если получено "exit", закрываем соединение и завершаем функцию
                    print("Received 'exit', closing connection...")
                    client_socket.close()
                    server_socket.close()
                    return
                
                # Для любых других строк отправляем их обратно клиенту
                client_socket.sendall(data.encode('utf-8'))
                
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            # Закрываем соединение с клиентом
            client_socket.close()
            print("Connection closed")