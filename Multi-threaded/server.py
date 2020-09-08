import socket

from _thread import *
import threading

print_lock = threading.Lock()

def threaded_func(c):
  while True:
    data = c.recv(1024)
    if not data:
      print("No data found. Closing off connection...")
      print_lock.release()
      break
    data = data[::-1]
    c.send(data)
  c.close()

host = socket.gethostname()
port = 42069
s = socket.socket()
s.bind((host, port))

s.listen(5)
print("Server is listening...")

while True:
  c, addr = s.accept()
  print_lock.acquire()
  print(f"Connected to : {addr[0]} : {addr[1]}")
  start_new_thread(threaded_func, (c,))
s.close()