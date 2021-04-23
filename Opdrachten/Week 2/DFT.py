# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:12:08 2021

@author: bart.bozon
"""

import matplotlib.pyplot as plt
import numpy as np

maxarray=64
signaal =np.zeros((maxarray),dtype=float)
t=np.zeros((maxarray),dtype=float)
dt=1/0.64    # 1 sec


def DFT():
    for i in range (len(t)):
        t[i]=i*dt
    sinus=np.zeros((int(maxarray/2)),dtype=float)
    cosinus=np.zeros((int(maxarray/2)),dtype=float)
    ifft =np.zeros((maxarray),dtype=float)
    mag=np.zeros((int(maxarray/2)),dtype=float)
    f=np.zeros((int(maxarray/2)),dtype=float)
    for i in range(len(f)) :
        f[i]=i*1/(dt*maxarray)
    for k in range (int(maxarray/2)): 
        for i in range (len(t)):
            sinus[k]+=signaal[i]*np.sin(2*k*i*np.pi/len(t))/(maxarray/2)
            cosinus[k]+=signaal[i]*np.cos(2*np.pi*k*i/len(t))/(maxarray/2)
    cosinus[0]=cosinus[0]*0.5        
    for k in range (int(maxarray/2)): 
        mag[k]=(sinus[k]**2+cosinus[k]**2)**0.5
    fig,ax= plt.subplots()
    plt.scatter(t,signaal,s=4)
    plt.title ('Signaal')
    plt.xlabel('Tijd (s)')
    plt.ylabel('Amplitude ()')
    plt.show()   
    plt.scatter(f,mag,s=4)
    plt.title ('Fourier transformatie')
    plt.xlabel('Frequentie (Hz)')
    plt.ylabel('Amplitude ()')
    plt.show()    
    for k in range (int(maxarray/2)): 
        ifft =np.zeros((maxarray),dtype=float)
        for i in range (len(t)):
            ifft[i]+=sinus[k]*np.sin(2*k*i*np.pi/len(t))
            ifft[i]+=cosinus[k]*np.cos(2*np.pi*k*i/len(t))
        plt.plot(t,ifft)
    plt.title ('Inverse fourier transformatie')
    plt.xlabel('Tijd (s)')
    plt.ylabel('Amplitude ()')
    plt.show()   

#for i in range (len(t)):
#    signaal[i]=np.sin(2*np.pi*i/64)
#DFT()        
#
#for i in range (len(t)):
#    signaal[i]=np.sin(2*np.pi*i/64) + np.sin(3*2*np.pi*i/64)
#DFT()        
#
#for i in range (len(t)):
#    signaal[i]=np.sin(2*np.pi*i/64) + 1/3*np.sin(3*2*np.pi*i/64)+1/5*np.sin(5*2*np.pi*i/64)
#DFT()        
#
#for i in range (len(t)):
#    if i % 64 <32 : 
#        signaal[i]=1
#    else:
#        signaal[i]=-1
#DFT()        

# 1.1
#for i in range(len(t)):
#    signaal[i] = np.sin(2*np.pi*i/64) + np.sin(10*2*np.pi*i/64)
#DFT()

#1.2
#for i in range(len(t)):
#    signaal[i] = np.cos(3*np.pi*i/64)
#DFT()

#1.3 
#for i in range (len(t)):
#    signaal[i]=np.sin(1*np.pi*i/64)**10*(np.sin(5*2*np.pi*i/64))
#DFT()

#for i in range (len(t)):
#    signaal[i]=(np.sin(5*2*np.pi*i/64))
#DFT()

#1.4
#for i in range(len(t)):
#    if i % 64 < 32:
#        signaal[i] = i*5
#    else:
#        signaal[i] = 32-(5*i-32)
#
#DFT()


