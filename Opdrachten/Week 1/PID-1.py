# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:12:08 2021

@author: bart.bozon
"""

import matplotlib.pyplot as plt
import numpy as np

maxarray=1000
y=np.zeros((maxarray),dtype=float)  # positie
yv=np.zeros((maxarray),dtype=float) # snelheid
setpoint=np.zeros((maxarray),dtype=float)
t=np.zeros((maxarray),dtype=float)
stuuractie=np.zeros((maxarray),dtype=float)

def voer_simulate_uit(kp,ki,kd):
    dt = 0.01           # [s] 
    veerconstante = 10  # [N/m]
    massa = 0.1         # [kg]
    zwaartekracht_constante = 9.81 # [m.s-2]
    y[0]=-massa*zwaartekracht_constante/veerconstante
    prev_error=0    # nu nog niet gebruikt. Misschien handig voor d-actie?
    i_error=0       # nu nog niet gebruikt. Misschien handig voor i-actie?
    for i in range (maxarray-1):
        totale_kracht = -zwaartekracht_constante * massa - veerconstante*(y[i]-stuuractie[i])
        versnelling = totale_kracht / massa
        yv[i+1] = yv[i]+versnelling *dt
        y[i+1]=y[i]+yv[i+1]*dt
        t[i+1]=t[i]+dt
        #==============  HIER KOMT JOUW CODE ======================
        
        error=setpoint[i+1]-y[i+1]
        i_error=i_error+error*dt
        error_div=(error-prev_error)/dt
        stuuractie[i+1]=kp*error+ki*i_error+kd*error_div
        prev_error = error

        # stel dat we geen PID regelaar proberen, maar gewoon onze arm omhoog
        #stuuractie[i+1]=setpoint[i]
        
        #==============  EINDE JOUW CODE ==========================
        if stuuractie[i+1]<-1 :
            stuuractie[i+1]=-1
        if stuuractie[i+1]>1 :
            stuuractie[i+1]=1
            
    fig,ax= plt.subplots()
    plt.plot(t,y,t,setpoint)
    plt.title ('uitslag en setpoint')
    plt.xlabel('Tijd (s)')
    plt.ylabel('Amplitude ()')
    plt.show()    
    plt.plot(t,y,t,stuuractie)
    plt.title ('uitslag en stuuractie')
    plt.xlabel('Tijd (s)')
    plt.ylabel('Amplitude ()')
    plt.show()    

setpoint[100:]=0.5   

voer_simulate_uit (1,0,0)

voer_simulate_uit (10,10,1)

        
    
    
    
