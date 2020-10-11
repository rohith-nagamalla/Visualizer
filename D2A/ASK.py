import matplotlib.pyplot as plt
import numpy as num

# F1=int(input('Enter the frequency of carrier='))
# A=2
# siz=int(input('Enter the size of signal='))
# t=num.arange(0,siz,0.001)                                  # time with the sampling frequency 0.001
# x=A*num.sin(2*num.pi*F1*t)                                 # carrier Sine wave

# b=[]
# for i in range(siz+1):
#     b.append((i+0.0))
    
# u=[]                                                        # digital message signal
# for i in t: 
#     if(i==b[0]):
#         b.pop(0)
#         s=int(input())
#     u.append(s)                                             # creating the digital message signal  


# v=[]                                                        # carrier wave multiplied with square wave


# for i in range(len(t)):
#     v.append(A*num.sin(2*num.pi*F1*t[i])*u[i])              # multiplying the digital message with the carrier
    
# #PLOTTING MESSAGE CARRIER AND ASK

# plt.plot(t,u)
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.title('Square wave Pulses')
# plt.grid(True)
# plt.show()

# plt.plot(t,x);
# plt.xlabel('Time');
# plt.ylabel('Amplitude');
# plt.title('Carrier');
# plt.grid(True)
# plt.show()

# plt.plot(t,v)
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.title('ASK Signal')
# plt.grid(True)
# plt.show()

'''
sample input ---

Enter the frequency of carrier=10

Enter the frequency of pulse=2
'''
def ASK(input_digital_signal):
    digital_signal=list(input_digital_signal)
    
    F1=int(input('Enter the frequency of carrier='))
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
        v.append(A*num.sin(2*num.pi*F1*t[i])*u[i])              # multiplying the digital message with the carrier

    return [t,v]    
