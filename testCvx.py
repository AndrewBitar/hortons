import cvxEDA as ce
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
from random import randint

import socket               # Import socket module
from numpy import nan

def runningMax (m, size, numlists):
    runMax = 0
    for i in range(numlists):
        for j in range(size):
            if (i == j):
                if (m[i][j] > runMax):
                    runMax  = m[i][j]
    return runMax

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = "192.168.2.3"
port = 12345                # Reserve a port for your service.


s.connect((host, port))
timeIntervalString = s.recv(1024)

dataSize = 10
y = []
counter = 0
plt.ion()
x = []
tonic =[]
phasic=[]

for i in range(dataSize):
    tonic.append([])
    phasic.append([])

tonicMaxList = []
phasicMaxList = []
    
while True:
    counter = counter +1
    print(np.size(y, 0))
    if np.size(y, 0) > dataSize:
        y.remove(y[0])
        #y = np.delete(y, 0)
    #f = s.makefile()
    #for line in f.readlines():
    line = s.recv(4)
    print(1.0/float(line))
    y.extend([1.0/float(line)]) 
    #y.extend([randint(0,600)])#)
    #np.append(y, s.recv(1024),0) 
    
    if counter >10:
        #yn = st.zscore(y)
        yn = y
        
        if (yn[0] == nan):
            yn = np.zeros(yn.size())
    
        r, p, t, l, d, e, obj = ce.cvxEDA(yn, 1.0/2.0)
        #x = range(np.size(yn,0))
        x.append(counter-11)
        
        tonic[(counter-1)%10] = t
        phasic[(counter-1)%10] = r
        
        numLists = 10
        if (counter-10 < 10):
            numLists = counter-10
        #print "numlists: ",numLists
        tonicMax = runningMax(tonic,dataSize, numLists)
        phasicMax = runningMax(phasic,dataSize, numLists)
        
        tonicMaxList.append(tonicMax)
        phasicMaxList.append(phasicMax)
        
        print "x: ", counter-11, " tonicMax: ", tonicMax, " phasicMax: ", phasicMax
        
        plt.figure(1)
        plt.clf()
        #plt.ylim([0,0.01])
        #plt.plot(x,y,x,p)
        plt.plot(x,tonicMaxList)
        #plt.show(block=False)
        
        plt.pause(0.05)
        plt.figure(2)
        plt.clf()
        #plt.ylim([0,0.001])
        plt.plot(x,phasicMaxList)
        plt.pause(0.05)
        
    