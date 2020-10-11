import matplotlib.pyplot as plt
import numpy as num


def PSK(input_digital_signal):
    digital_signal=list(input_digital_signal)
    
    F1=6
    A=2
    siz = len(input_digital_signal)
    
    t=num.arange(0,siz,0.001)                                  # time with the sampling frequency 0.001
    x=A*num.sin(2*num.pi*F1*t)                                 # carrier Sine wave

    b=[]
    for i in range(siz+1):
        b.append((i+0.0))

    u=[]                                                        # digital message signal
    for i in t: 
        if(i==b[0]):
            b.pop(0)
            s=digital_signal[0]
            digital_signal.pop(0)
        u.append(s)                                             # creating the digital message signal 

    v=[]                                                        # carrier wave multiplied with square wave
    for i in range(len(t)):
        if(u[i]==1):
            v.append(A*num.sin(2*num.pi*F1*t[i]))               # if the signal is 1, then higher frequency f+f/2
        else:
            v.append(A*num.sin(2*num.pi*F1*t[i])*(-1))          # else lower frequncy f-f/2
    return [t,v,u,x]


