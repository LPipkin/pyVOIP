import socket
import threading
import os    

def fileSendClientMain():
    host = '98.230.39.219'
    port = 8002


    s = socket.socket()
    s.connect((host, port))

    filename = s.recv(1024)
    if os.path.isfile(filename):
        s.send("EXISTS")
        with open(filename, 'rb') as f:
            bytesToSend = f.read(1024)
            s.send(bytesToSend)
            while bytesToSend != "":
                bytesToSend = f.read(1024)
                s.send(bytesToSend)
    else:
        s.send("ERR ")

    s.close()

sif __name__ == '__main__':
    fileSendClientMain()