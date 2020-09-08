import socket

s = socket.socket()
host = socket.gethostname()
port = 42069

s.bind((host, port))

print("Waiting for connection...")
s.listen(5)

while True:
  conn, addr = s.accept()
  print(f"Got connection from {addr}")
  conn.send('Hello, Thanks for connecting'.encode('utf-8'))
  conn.close()
