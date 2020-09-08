import socket
from _thread import *

server_socket = socket.socket()

host = socket.gethostname()
port = 42069

ThreadCount = 0

try:
  server_socket.bind((host, port))
except socket.error as e:
  print(str(e))

print("Waiting from connection...")
server_socket.listen(5)

def client_thread(connection):
  connection.send("Welcome to the server".encode('utf-8'))
  while True:
    data = connection.recv(2048)
    reply = "Hello I am a server " + data.decode('utf-8')
    if not data:
      break
    connection.sendall(reply.encode('utf-8'))
  connection.close()

while True:
  client, address = server_socket.accept()
  print(f"connected to address: {address[0]}:{address[1]}")
  start_new_thread(client_thread, (client,))
  ThreadCount +=1
  print(f"ThreadNumber {ThreadCount}")

server_socket.close()
