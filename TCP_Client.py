#TCP Client
from socket import *
import time
import PKI_Module
import pickle
from PKI_Manual import dataEncode
import json
def TCP_Client(HOST, PrivateKey, PublicKey, data):
    PORT = 2001
    BUFSIZ=4000
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)

    print "Before connect"
    tcpCliSock.connect(ADDR)
    print "After connect"


    while True:
        encryptMsg = dataEncode(data, PrivateKey)
        encodedMsg = encryptMsg +'\n'+ PublicKey + '\n' + time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())

        if tcpCliSock.send(encodedMsg):
            break

    tcpCliSock.close()