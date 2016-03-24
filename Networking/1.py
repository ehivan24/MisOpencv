'''
Created on Mar 19, 2015

@author: edwingsantos
'''

import socket
import sys
s = socket.socket()

s.bind(("localhost", 9999))
s.listen(10)

while True:
    sc, address = s.accept()
    print address
    i = 1
    f = open("1.pdf",'wb')
    while True:
        l = sc.recv(1024)
        while(l):
            f.write(l)
            l = sc.recv(1024)
    f.close()
s.close() 


        
    