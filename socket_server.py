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
    print ("Received from client: " + data)
    while conn.send(input().encode()) != 'stop':
        l = conn.send(input().encode())
        print ("Sent to client: ", l)
    else:
        conn.close()
        print ("Connection closed")