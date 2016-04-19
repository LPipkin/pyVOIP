
import socket

def fileReceiveClientMain():
    host = '98.230.39.219'
    port = 8000

    s = socket.socket()
    s.connect((host, port))

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

    s.close()
    

if __name__ == '__main__':
    fileReceiveClientMain()