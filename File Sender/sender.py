import socket
import tqdm
import os

SEPERATOR = "<SEPERATOR>"
BUFFER_SIZE = 4096

host = socket.gethostname()
port = 42069

file_name = "sendfile.csv"
file_size = os.path.getsize(file_name)

s = socket.socket()
s.connect((host, port))

s.send(f"{file_name}{SEPERATOR}{file_size}".encode('utf-8'))

progress = tqdm.tqdm(range(
    file_size), f"Sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
with open(file_name, "rb") as f:
    for _ in progress:
        byte_read = f.read(BUFFER_SIZE)
        if not byte_read:
            break
        s.sendall(byte_read)
        progress.update(len(byte_read))

s.close()
