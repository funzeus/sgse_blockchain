#TCP Client
from socket import *
import PKI_Module
import pickle
from PKI_Manual import dataEncode

def TCP_Client(HOST, PrivateKey, PublicKey):
    PORT = 2001
    BUFSIZ=1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)


    print "Before connect"
    tcpCliSock.connect(ADDR)
    print "After connect"

    while True:
        data = "dataaa"

        #Encryption
        encryptMsg = dataEncode(data, PrivateKey)
        encodedMsg = encryptMsg +' '+ PublicKey

        if tcpCliSock.send(encodedMsg):
            break

    tcpCliSock.close()

