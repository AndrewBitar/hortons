import cvxEDA as ce
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
from random import randint
        # Import socket module
from scipy import nan
import re


from select import select
from socket import socket
import sys

sock = socket()
sock.connect(('192.168.2.3', 12345))
sock.setblocking(False)

def readlines(sock, recv_buffer=4096):
    data = True
    while data:
        data = sock.recv(recv_buffer)
        yield data
    return

dataSize = 10
y = []
counter = 0
plt.ion()

while True:
    readable, writable, exceptional = select([sock], [], [sock], 1)
    if not (readable or writable or exceptional):
        print >>sys.stderr, '  timed out, do some other work here'
        continue
    if readable:
        for line in readlines(sock):
            print line
            if re.search(r"^Time interval: (.*)$", line):
                print line
            else:
                print(1.0/float(line))
                y.extend([float(1.0/float(line))])
                counter += 1
    
        
            
    #y.extend([randint(0,600)])#)
    #np.append(y, s.recv(1024),0) 
        
    #print "yn.size: ", yn.size
    #print "yn before: ",yn
    
        
    if counter>10:
        print "counter: ", counter
        yn = st.zscore(y)
        if (yn[0] == nan):
            yn = np.zeros(yn.size)
        print "yn: ",yn
        r, p, t, l, d, e, obj = ce.cvxEDA(yn, 0.05)
        x = range(r.size)
        
        plt.figure(1)
        plt.clf()
        plt.plot(x,yn)
        
        plt.figure(2)
        plt.clf()
    #plt.ylim([0,0.01])
    #plt.plot(x,y,x,p)
        plt.plot(x,t)
        #plt.show(block=False)
        
        
        plt.figure(3)
        plt.clf()
        #plt.ylim([0,0.001])
        plt.plot(x,r)
        plt.pause(0.05)
    
    #counter += 1
    