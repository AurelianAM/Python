from factura import Factura
import socket


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

serverSocket.bind(('127.0.0.1', 35780))

invoiceList = []

serverSocket.listen()

while True:
    connSocket, connAdress = serverSocket.accept()
    print(f'Connection established with {connAdress}')
    # while True:
    consume = int(connSocket.recv(1024).decode('utf-8'))
    invoiceList.append(Factura(consume))
    connSocket.sendall(bytes(str(invoiceList[-1]), 'utf-8'))
    connSocket.close()