#!/usr/bin/python3
#!encoding='utf-8'

import socket
import time
import codecs
import threading

from protocol.gurgle import *
from core.serviceMain import *

if __name__ == '__main__':
    SERVICE_PORT = 40097
    ADDR = ('',SERVICE_PORT)
    sevSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sevSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sevSocket.bind(ADDR)
    sevSocket.listen(5)
    while True:
        clientSocket,addr = sevSocket.accept()
        newThread = ServiceThread()
        newThread.setup(clientSocket,addr)
        newThread.start()

