import socket
from _thread import *

server_socket = socket.socket()
client_socket = socket.socket()

host = socket.gethostname()
initiation_port = int(input("Enter initiation port: "))

try:
  server_socket.bind((host, initiation_port))
except socket.error as e:
  print(str(e))

print("Socket start listening...")
server_socket.listen(1)

def client_listener():
  client, address = server_socket.accept()
  print(f"connected to address: {address[0]}:{address[1]}")
  while True:
    data = client.recv(2048)
    print("\nClient >> " + data.decode('utf-8'))
    if not data:
      break
  client.close()
  server_socket.close()

start_new_thread(client_listener, ())

def client_speaker():
  connection_port = int(input("Enter connection port: "))
  while True:
    try:
      client_socket.connect((host, connection_port))
      while True:
        data = input(">> ")
        client_socket.send(data.encode('utf-8'))
    except socket.error:
      continue
    except KeyboardInterrupt:
      break
  client_socket.close()

start_new_thread(client_speaker, ())

try:
  while True: continue
except KeyboardInterrupt:
  pass
