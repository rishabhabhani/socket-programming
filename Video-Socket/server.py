import socket
import cv2
import struct
import pickle

host = socket.gethostname()
port = 42069

s = socket.socket()
s.bind((host, port))

s.listen(10)

while True:
    conn, addr = s.accept()
    if conn:
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            img, frame = cam.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            conn.sendall(message)
            cv2.imshow('SeverSide Feed', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                conn.close()
                cam.release()
