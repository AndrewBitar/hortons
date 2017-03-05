from select import select
from socket import socket

sock = socket()
sock.connect(('192.168.2.3', 12345))

def readlines(sock, recv_buffer=4096):
    data = True
    while data:
        data = sock.recv(recv_buffer)
        yield data
    return

while True:
    readable, writable, exceptional = select([sock], [], [sock], 1)
    if not (readable or writable or exceptional):
        print >>sys.stderr, '  timed out, do some other work here'
        continue
    if readable:
        for line in readlines(sock):
            print line
