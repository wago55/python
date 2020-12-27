from ftplib import FTP

HOST = '10.0.0.1'
PORT = 10021
USER = 'masaki'
PASSWORD = '19990501'

with FTP() as ftp:
    ftp.connect(HOST,PORT)
    ftp.login(USER,PASSWORD)
    ftp.cwd('/Develope/python3')
    with open('/Users/wago55/Desktop/a.txt', 'rb') as f:
        ftp.storbinary('STOR a.txt', f)
