import socket
import cv2
import struct
import pickle

host = socket.gethostname()
port = 42069

s = socket.socket()
s.connect((host, port))

data = b""
payload_size = struct.calcsize("Q")
while True:
    while len(data) < payload_size:
        packet = s.recv(4096)
        if not packet:
            break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += s.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("Received feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

s.close()

while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
