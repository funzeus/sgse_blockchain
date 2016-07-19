#TCP Client
from socket import *
import PKI_Module
import pickle

def TCP_Client(HOST):
    PORT = 2001
    BUFSIZ=1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)

    pki = PKI_Module.pkiModule(1024)

    print "Before connect"
    tcpCliSock.connect(ADDR)
    print "After connect"

    while True:
        data = "dataaa"

        # PKI module
        encryptData = pki.dataEncryption(data)
        temp = pickle.dump(pki.pubKey)
        print temp
        if tcpCliSock.send(temp):
            tcpCliSock.send(encryptData)
            break

    tcpCliSock.close()

