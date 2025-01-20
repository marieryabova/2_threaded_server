import socket
import logging
import datetime

# Настройка логирования
logging.basicConfig(filename='client.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Подключено к серверу {host}:{port}")
            logging.info(f"Подключено к серверу {host}:{port}")
            while True:
                message = input("Введите сообщение (или 'exit' для выхода): ")
                if message == 'exit':
                    break
                s.sendall(message.encode())
                data = s.recv(1024)
                print(f"Получено от сервера: {data.decode()}")
                logging.info(f"Получено от сервера: {data.decode()}")
        except Exception as e:
            print(f"Ошибка подключения или работы клиента: {e}")
            logging.error(f"Ошибка подключения или работы клиента: {e}")
        finally:
            print("Клиент отключился")
            logging.info("Клиент отключился")


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 65432
    start_client(host, port)