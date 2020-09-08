import socket

s = socket.socket()
host = socket.gethostname()
port = 42069

s.connect((host, port))
print(s.recv(2048).decode('utf-8'))

s.close()