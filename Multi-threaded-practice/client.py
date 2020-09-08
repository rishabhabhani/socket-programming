import socket

client_socket = socket.socket()

host = socket.gethostname()
port = 42069

print("Waiting for connection..")

try:
  client_socket.connect((host, port))
except socket.error as e:
  print(str(e))

response = client_socket.recv(2048)
print(response.decode('utf-8'))
while True:
  data = input(">> ")
  client_socket.send(data.encode('utf-8'))
  response = client_socket.recv(1024)
  print(response.decode('utf-8'))

client_socket.close()