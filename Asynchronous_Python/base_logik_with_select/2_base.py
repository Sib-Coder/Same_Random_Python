import socket
from select import select

to_monitor= []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))

server_socket.listen()


def accept_coonetion(server_socket):
    client_socket, addr = server_socket.accept()
    print( 'Connection from ', addr)

    to_monitor.append(client_socket)

def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        ready_to_read, _, _= select(to_monitor, [], []) #read, write, errors
        #мониторит список сокетов на доступность на чтение
        for sock in ready_to_read:
            if sock is server_socket:
                accept_coonetion(sock)
            else:
                send_message(sock)

if __name__=="__main__":
    to_monitor.append(server_socket)
    event_loop()
