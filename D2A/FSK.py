import matplotlib.pyplot as plt
import numpy as num

F1=int(input('Enter the frequency of carrier='))
A=2;
siz=int(input('Enter the size of signal='))
t=num.arange(0,siz,0.001)                                  # time with the sampling frequency 0.001
x=A*num.sin(2*num.pi*F1*t)                                 # carrier Sine wave

b=[]
for i in range(siz+1):
    b.append((i+0.0))

u=[]                                                        # digital message signal
for i in t: 
    if(i==b[0]):
        b.pop(0)
        s=int(input())
    u.append(s)                                             # creating the digital message signal  


v=[]                                                        # carrier wave multiplied with square wave


for i in range(len(t)):
    if(u[i]==1):
        v.append(A*num.sin(3*num.pi*F1*t[i]))               # if the signal is 1, then higher frequency f+f/2
    else:
        v.append(A*num.sin(1*num.pi*F1*t[i]))               # else lower frequncy f-f/2


#PLOTTING MESSAGE CARRIER AND FSK

plt.plot(t,u)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.grid(True)
plt.show()

plt.plot(t,x);
plt.xlabel("time");
plt.ylabel("Amplitude");
plt.title("Carrier");
plt.grid(True)
plt.show()


plt.plot(t,v);
plt.xlabel("t");
plt.ylabel("y");
plt.title("FSK");
plt.grid(True)
plt.show()
'''Enter the frequency of carrier=10
Enter the frequency of pulse=2'''




