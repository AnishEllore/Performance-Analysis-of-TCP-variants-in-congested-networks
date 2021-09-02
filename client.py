#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/client.py
# Simple Zen-of-Python client that asks three questions then disconnects.

import argparse, random, socket, zen_utils, time, datetime

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    aphorisms = list(zen_utils.aphorisms)
    f = open("input.txt",'rb')
    time.sleep(10)
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return
    message = f.read(65535)
    while (message):
        sock.sendall(message)
        message = f.read(65535)
    sock.shutdown(socket.SHUT_WR)
    f.close()
    '''
    f=open("sent.mkv",'wb')
    temp = sc.recv(1024)
        
    while (temp):
        f.write(temp)
        temp = sc.recv(1024)
        #print('  Incoming sixteen-octet message:', repr(message))
    f.close()
    '''
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    client(address, args.e)
