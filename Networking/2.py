'''
Created on Apr 2, 2015

@author: edwingsantos
'''


import socket
import sys

s = socket.socket()

s.connect(("localhost", 9999))
