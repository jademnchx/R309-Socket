import socket

def recep():
    print ("Waiting for connection")
    
    
if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 10000))
    print ("Server started")
    server_socket.listen(1)
    conn, address = server_socket.accept()
    data = conn.recv(1024).decode()
    conn.send('stop'.encode())
    print ("Received: " + data)
    conn.close()