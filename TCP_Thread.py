#!/usr/bin/python
import thread, time
from TCP_Client import TCP_Client
from TCP_Server import TCP_Server

thread.start_new_thread(TCP_Server, ())
time.sleep(1)


while True:
    input = raw_input('<')
    if(input =='send'):
        HOST = raw_input('connect ip : ')
        thread.start_new_thread(TCP_Client,(HOST,))
        time.sleep(1)

