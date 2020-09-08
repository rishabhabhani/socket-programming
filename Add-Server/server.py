import socket

host = socket.gethostname()
port = 42069
s = socket.socket()
s.bind((host, port))

s.listen(5)

conn, addr = s.accept()
print(f"Connection by {addr}")

while True:
  data = conn.recv(1024).decode('utf-8')
  if(data == "-1"):
    print("Breaking connection with the client...")
    conn.sendall("Breaking connection with the server...".encode('utf-8'))
    break
  d = data.split(",")
  try:
    data_add = int(d[0]) + int(d[1])
    conn.sendall(str(data_add).encode('utf-8'))
  except:
    break
conn.close()