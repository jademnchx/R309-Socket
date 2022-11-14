import socket

def recep():
    print ("Receiving")

if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 10000))
    print ("Connected to server")
    t=client_socket.send(input().encode())
    while t != 'stop':
        t
    else :
        client_socket.close()
        print ("Connection closed")
    data = client_socket.recv(1024).decode()
    print ("Received from server: ", data)
