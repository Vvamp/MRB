# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:12:08 2021

@author: bart.bozon
"""

import matplotlib.pyplot as plt
import numpy as np

maxarray=1000
x=np.zeros((maxarray),dtype=float)  # positie
xv=np.zeros((maxarray),dtype=float) # snelheid
setpoint=np.zeros((maxarray),dtype=float)
t=np.zeros((maxarray),dtype=float)
stuuractie=np.zeros((maxarray),dtype=float)

def voer_simulate_uit(kp,ki,kd):
    dt = 0.01           # [s] 
    massa = 0.1         # [kg]
    veerconstante = 10  # [N/m]
    zwaartekracht_constante = 9.81 # [m.s-2]
    delay=10
    montage_offset=0
    x[0]=0
    wrijvingscoeeficient = 2
    prev_error=0    # nu nog niet gebruikt. Misschien handig voor d-actie?
    i_error=0       # nu nog niet gebruikt. Misschien handig voor i-actie?
    for i in range (maxarray-1-delay):
        totale_kracht = -zwaartekracht_constante * massa - veerconstante*(x[i]-stuuractie[i])-wrijvingscoeeficient *xv[i]
        versnelling = totale_kracht / massa
        xv[i+1] = xv[i]+versnelling *dt
        x[i+1]=x[i]+xv[i+1]*dt
        t[i+1]=t[i]+dt
        #==============  HIER KOMT JOUW CODE ======================
        error=setpoint[i+1]-x[i+1]
        i_error+=error*dt        
        stuuractie[i+1+delay]=kp*error+kd*(error-prev_error)/dt+ki*i_error
        prev_error=error
        #==============  EINDE JOUW CODE ==========================
        if stuuractie[i+1]<-2 :
            stuuractie[i+1]=-2
        if stuuractie[i+1]>2 :
            stuuractie[i+1]=2
            
    fig,ax= plt.subplots()
    plt.plot(t[:maxarray-delay],x[:maxarray-delay],t[:maxarray-delay],setpoint[:maxarray-delay])
    plt.title ('uitslag en setpoint')
    plt.xlabel('Tijd (s)')
    plt.ylabel('Amplitude ()')
    plt.show()    
    plt.plot(t[:maxarray-delay],x[:maxarray-delay],t[:maxarray-delay],stuuractie[:maxarray-delay])
    plt.title ('uitslag en stuuractie')
    plt.xlabel('Tijd (s)')
    plt.ylabel('Amplitude ()')
    plt.show()    

setpoint[100:]=0.5   

 
voer_simulate_uit (2.75,0,0)
Ku=2.75
Tu=0.8

# classic PID
Kp_new=0.6*Ku
Ki_new=1.2*Ku/Tu
Kd_new=0.075*Ku*Tu
voer_simulate_uit (Kp_new,Ki_new,Kd_new)

# No overshoot
Kp_new=0.2*Ku
Ki_new=0.4*Ku/Tu
Kd_new=0.066*Ku*Tu
voer_simulate_uit (Kp_new,Ki_new,Kd_new)




        
    
    
    
