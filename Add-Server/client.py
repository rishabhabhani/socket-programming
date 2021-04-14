import socket

host = 'raspberrypi.local'
port = 42069

s = socket.socket()
s.connect((host, port))

while True:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = f"{a},{b}"
    print(f"Sending {c} to server...")

    if a == "-1" or b == "-1":
        s.sendall("-1".encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(data)
        break

    else:
        s.sendall(c.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(int(data))

s.close()
