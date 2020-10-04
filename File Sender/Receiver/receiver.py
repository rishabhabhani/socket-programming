import socket
import tqdm
import os

host = socket.gethostname()
port = 42069

BUFFER_SIZE = 4096
SEPERATOR = "<SEPERATOR>"

s = socket.socket()
s.bind((host, port))

s.listen(5)

client_socket, addr = s.accept()

received = client_socket.recv(BUFFER_SIZE).decode('utf-8')
file_name, file_size = received.split(SEPERATOR)

file_name = "receivedfile.csv"
file_size = int(file_size)

progress = tqdm.tqdm(range(
    file_size), f"Receiving {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
with open(file_name, "wb") as f:
    for _ in progress:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))

client_socket.close()
s.close()
