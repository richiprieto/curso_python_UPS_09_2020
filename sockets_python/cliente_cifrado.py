import socket
import pyDes
HOST = '127.0.0.1'  # IP del servidor
PORT = 65432        # Puerto del servidor
password = "password"
k = pyDes.des(password, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
mensaje = "Esto es un mensaje cifrado"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(k.encrypt(mensaje))
    data = s.recv(1024)

print('Recibido', repr(k.decrypt(data)))
