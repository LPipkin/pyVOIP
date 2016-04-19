
import socket
import threading
import os

def RetrFile(name, s):
    filename = "test_recording.wav"
    s.send(filename)
    data = s.recv(1024)
    if data[:6] == 'EXISTS':
        f = open(filename, 'wb')
        data = s.recv(1024)
        f.write(data)
        while data != '':
            data = s.recv(1024)
            f.write(data)
        print "Download Complete!"
        f.close()
    else:
        print "File Does Not Exist!"

def Main():
    host = '192.168.2.20'
    port = 8002

    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print("Receive Server Started")
    while True:
        c, addr = s.accept()
        print "client connected ip:<" + str(addr) + ">"
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
         
    s.close()
    

if __name__ == '__main__':
    Main()