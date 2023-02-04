import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# clientSocket.connect(('127.0.0.1', 35780))
# print('Connected to server...')

while True:
    clientSocket.connect(('127.0.0.1', 35780))
    print('Connected to server...')
    consume = input('Input the consume: ')
    clientSocket.sendall(bytes(consume, 'utf-8'))
    serverMsg = clientSocket.recv(1024).decode('utf-8')
    print(serverMsg)

    clientSocket.close()   