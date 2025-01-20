import socket
import threading
import time
import tqdm

def scan_port(host, port, open_ports):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((host, port))
            open_ports.append(port)
            print(f"Порт {port} открыт")
        except (ConnectionRefusedError, socket.timeout):
            pass

def scan_ports_parallel(host, start_port, end_port):
    open_ports = []
    threads = []
    with tqdm.tqdm(total=end_port - start_port + 1, desc="Сканирование портов") as pbar:
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(host, port, open_ports))
            thread.start()
            threads.append(thread)
            time.sleep(0.01)
            pbar.update(1)
        for thread in threads:
            thread.join()
    open_ports.sort()
    print("\nОткрытые порты:", open_ports)

if __name__ == "__main__":
    host = input("Введите имя хоста или IP-адрес: ")
    start_port = int(input("Введите начальный порт: "))
    end_port = int(input("Введите конечный порт: "))
    scan_ports_parallel(host, start_port, end_port)