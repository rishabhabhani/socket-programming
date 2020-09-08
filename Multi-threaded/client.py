import socket

host = socket.gethostname()
port = 42069
s = socket.socket()
s.connect((host, port))

message = "Hello World"

while True:
  s.send(message.encode('utf-8'))
  data = s.recv(1024).decode('utf-8')
  print(f'Received from the server : {data}')

  ans = input('Do you want to continue? (y/n)')
  if 'y' in ans:
    continue
  else:
    break
s.close()