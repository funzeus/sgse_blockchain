#!/usr/bin/python
import thread, time
from TCP_Client import TCP_Client
from TCP_Server import TCP_Server
from PKI_Manual import keyGeneration, keyTostr
import json

def TCP_Thread():
    Sender = '163.239.200.188'
    thread.start_new_thread(TCP_Server, ())
    time.sleep(1)

    publicKey, privateKey = keyGeneration(2**256)
    publicKey = keyTostr(publicKey)

    while True:
        input = raw_input('<')
        if(input =='send'):
            HOST = raw_input('connect ip : ')
            amount = raw_input('amount : ')
            msg = raw_input('msg : ')
            bitcoin = {
                'recv': HOST,
                'sender': publicKey,
                'amount': amount,
                'msg': msg
            }
            jsonBit = json.dumps(bitcoin)
            thread.start_new_thread(TCP_Client, (HOST, privateKey, publicKey,jsonBit,))
            time.sleep(1)

TCP_Thread()