"""
Usage python 8.py --host=www.python.org --port=80 --file=1_7_socket_errors.py
"""



import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='Socket Error Ex')
    parser.add_argument('--host', action="store", dest="host", required=False )
    parser.add_argument('--port', action="store", dest="port", required=False )
    parser.add_argument('--file', action="store", dest="file", required=False )
    
    givenArgs = parser.parse_args()
    host = givenArgs.host
    port = givenArgs.port
    filename = givenArgs.file
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error creating socket: %s" %e
        sys.exit(1)
        
    
    try: 
        s.connect((host, int(port)))
    except socket.gaierror, e:
        print "Address-related error connectin server %s" %e
        sys.exit(1)
    except socket.error, e:
        print "Connection error %s" %e
        sys.exit(1)
        
    try: 
        s.sendall("GET %s HTTP/1.0\r\n\r\n" %filename)
    except socket.error, e:
        print "Error sending data %s" %e
        sys.exit(1)
    
    while True:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print "Error receiving Data %s" %e
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf)
        

main()
    