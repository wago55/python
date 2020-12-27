import socket

HOST = "10.0.0.1"
PORT = 8001


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.bind((HOST, PORT))
    while True:
        server.listen()       
        client, addr = server.accept()
        
        with client:   
            receive_message = client.recv(4096).decode()
            print(f'message:{receive_message}')

            if receive_message == "end\r\n":
                break
                
            message = 'I am a socket server...\n'
            message_en = message.encode()
            client.send(message_en)

        
    server.close()

