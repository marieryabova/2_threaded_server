import socket
import threading
import datetime
import logging

# Настройка логирования
logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client(client_socket, address):
    try:
        print(f"Подключился клиент: {address}")
        logging.info(f"Подключился клиент: {address}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Получено от {address}: {message}")
            logging.info(f"Получено от {address}: {message}")
            client_socket.sendall(data)  # Отправляем обратно то же сообщение
    except Exception as e:
        print(f"Ошибка обработки клиента {address}: {e}")
        logging.error(f"Ошибка обработки клиента {address}: {e}")
    finally:
        client_socket.close()
        print(f"Клиент {address} отключился")
        logging.info(f"Клиент {address} отключился")

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Сервер запущен на {host}:{port}")
        logging.info(f"Сервер запущен на {host}:{port}")
        while True:
            client_socket, address = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.daemon = True
            client_thread.start()

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 65432
    start_server(host, port)