import socket



if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 10000))
    print ("Connected to server")
    client_socket.send('start'.encode())
    data = client_socket.recv(1024).decode()
    client_socket.close()