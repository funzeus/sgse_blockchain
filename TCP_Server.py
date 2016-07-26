#TCP Server
from socket import *
from time import ctime
import PKI_Manual

def TCP_Server():
    HOST='163.239.200.183'
    PORT=2001
    BUFSIZ=10
    ADDR=(HOST,PORT)

    tcpSerSock = socket(AF_INET,SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print 'waiting for connection...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '....conneted from:', addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if tcpCliSock.send('[%s] %s' %(ctime(), data)):
                print data
                break

        tcpCliSock.close()
    tcpSerSock.close()


