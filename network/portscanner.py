import socket
import time

try:
    max_port = 100
    min_port = 0

    target_host = input('Input target host adress or host name: ')

    start = time.time()

    for port in range(min_port,max_port):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            return_code = s.connect_ex((target_host,port))
    
        if return_code == 0:
            print(f"Port {port} open. let's attack.")

    print('port scan is finished.')

    end = time.time()
    time = end - start

    print(f"We took time to scan port {time}")

except KeyboardInterrupt:
    print("KeyboardInterrupt")

except socket.gaierror:
    print("Error. Host name or host adress is invailed")