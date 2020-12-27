import socket

HOST = "10.0.0.1"
PORT = 8001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    message_list = ['GET / HTTP/1.1', 'hsot:10.0.0.1']

    send_message = ""

    for message in message_list:
        send_message += message + "\n"
    send_message += "\n"

    send_binary = send_message.encode()
    client.send(send_binary)

    receive_message = []
    byte_recd = 0
    BUFSIZE = 4096
    while byte_recd < BUFSIZE:
        receive = client.recv(min(BUFSIZE - byte_recd, 2048))
        if receive == b"":
            break
            
        receive_message = receive.decode()
        byte_recd += len(receive) 
        
print(f'{receive_message}')
