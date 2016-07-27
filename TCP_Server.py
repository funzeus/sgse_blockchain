#TCP Server
from socket import *
from time import ctime
import json
from PKI_Manual import dataDecode, strTokey



def TCP_Server():
    HOST='163.239.200.188'
    PORT=2001
    BUFSIZ=4000
    ADDR=(HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print 'waiting for connection...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '....conneted from:', addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            recvData = data.split('\n')
            if len(recvData) > 1:
                recvPublicKey = strTokey(recvData[1])
                print "Data :  " + recvData[0]
                print "Key : " + recvData[1]
                print "Time : " + recvData[2]
                decodedData = dataDecode(recvData[0], recvPublicKey)
                #dict = json.loads(decodedData)
                #print dict['amount']


        tcpCliSock.close()
    tcpSerSock.close()

