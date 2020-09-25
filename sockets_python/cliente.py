import socket

HOST = '127.0.0.1'  # IP del servidor
PORT = 65432        # Puerto del servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hola Mundo, acabo de conectarme, por sockets')
    data = s.recv(1024)

print('Recibido', repr(data))
