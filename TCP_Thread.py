#!/usr/bin/python
import thread, time
from TCP_Client import TCP_Client
from TCP_Server import TCP_Server
from PKI_Manual import keyGeneration, keyTostr


thread.start_new_thread(TCP_Server, ())
time.sleep(1)

publicKey, privateKey = keyGeneration(2**256)
publicKey = keyTostr(publicKey)

while True:
    input = raw_input('<')
    if(input =='send'):
        HOST = raw_input('connect ip : ')
        thread.start_new_thread(TCP_Client, (HOST, privateKey, publicKey,))
        time.sleep(1)

