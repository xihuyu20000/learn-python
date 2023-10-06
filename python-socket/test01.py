import socket

HOST, PORT = '0.0.0.0', 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
print(f'Server {HOST} is listening on {PORT}')

while True:
    conn, addr = sock.accept()
    print(f'connect from {addr}')

    while True:
        data = conn.recv(1024)
        print(addr, ' send data: ', data)
        if data == b'':
            conn.sendall(b'not null\r\n')
        elif data ==b'exit':
            conn.close()
            break
        else:
            conn.sendall(data)
conn.close()