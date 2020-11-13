from D2A.ASK import ASK
from D2A.PSK import PSK
from D2A.FSK import FSK

import matplotlib.pyplot as plt


def plot2(li,option):
    if option==8:
        t,v,u,x = ASK(li)
        plt.subplot(3,1,1)
        plt.plot(t,u)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Square wave Pulses')
        plt.grid(True)
        plt.subplot(3,1,2)
        plt.plot(t,x)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Carrier Signal')
        plt.grid(True)        
        plt.subplot(3,1,3)
        plt.plot(t,v)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('ASK Signal')
        plt.grid(True)
        plt.show()

    elif option==9:
        t,v,u,x = FSK(li)
        plt.subplot(3,1,1)
        plt.plot(t,u)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Square wave Pulses')
        plt.grid(True)
        plt.subplot(3,1,2)
        plt.plot(t,x)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Carrier Signal')
        plt.grid(True)
        plt.subplot(3,1,3)
        plt.plot(t,v)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('FSK Signal')
        plt.grid(True)
        plt.show()


    else:
        t,v,u,x = PSK(li)
        plt.subplot(3,1,1)
        plt.plot(t,u)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Square wave Pulses')
        plt.grid(True)
        plt.subplot(3,1,2)
        plt.plot(t,x)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Carrier Signal')
        plt.grid(True)
        plt.subplot(3,1,3)
        plt.plot(t,v)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('PSK Signal')
        plt.grid(True)
        plt.show()    

    
