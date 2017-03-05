import cvxEDA as ce
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
from random import randint

import socket               # Import socket module
from scipy import nan


s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = "192.168.2.3"
port = 12345              # Reserve a port for your service.


s.connect((host, port))

timeIntervalString = s.recv(1024)
s.setblocking(False)

dataSize = 10
y = []
counter = 0
plt.ion()

    
while True:
    
    
    while True:
         
        try:
            line=s.recv(4)
        except socket.error, exc:
            break
        print line
        print(1.0/float(line))
        y.extend([float(1.0/float(line))])
        counter += 1
    
         
            
    #y.extend([randint(0,600)])#)
    #np.append(y, s.recv(1024),0) 
        
    #print "yn.size: ", yn.size
    #print "yn before: ",yn
    
        
    if counter>100:
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
    