#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/client.py
# Simple Zen-of-Python client that asks three questions then disconnects.

import argparse, random, socket, zen_utils, time, datetime

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    f = open("output.txt",'wb')
    aphorisms = list(zen_utils.aphorisms)
    time.sleep(10)
    a=datetime.datetime.now();
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return
    message = sock.recv(65535)
    while (message):
        #print('hello ',message)
        f.write(message)
        message=sock.recv(65535)

    f.close()
    b=datetime.datetime.now()
    c=b-a
    print(c.seconds)
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
