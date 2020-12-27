import socket
import threading
import time

try:

    scan_range = [0,100]

    threads = []
    ports = []
    isopen = []

    count = 0

    def Run(port, count):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                return_code = s.connect_ex((target_host,port))
     
        if return_code == 0:
            isopen[count] = 1

    target_host = input('Input target host adress or host name: ')

    start = time.time()

    for port in range(scan_range[0], scan_range[1]):
        ports.append(port)
        isopen.append(0)
        thread = threading.Thread(target=Run, args=(port, count))
        thread.start()
        threads.append(thread)
        count += 1

    for i in range(len(threads)):
        threads[i].join()
        if isopen[i] == 1:
            print(f"{ports[i]} is open. let's attack.") 

    print('port scan is finished')

    end = time.time()
    time = end - start

    print(f"We took time to scan port {time}")

except KeyboardInterrupt:
    print("KeyboardInterrupt")

except socket.gaierror:
    print("Error. Host name or host adress is invailed")
