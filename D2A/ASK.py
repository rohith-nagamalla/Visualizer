import matplotlib.pylab as plt
import numpy as num

F1=int(input('Enter the frequency of carrier='))
A=2
siz=int(input('Enter the size of signal='))
t=num.arange(0,siz,0.001)
x=A*num.sin(2*num.pi*F1*t)#Carrier Sine wave
u=[]#Message signal
b=[]
for i in range(siz+1):
    b.append((i+0.0))
    # u.append(int(input()))
# b=[0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]
s=1
# print(t)
for i in t: 
    if(i==b[0]):
        b.pop(0)
        s=int(input())
        #print(s,i,b)
    u.append(s)
v=[]#Sine wave multiplied with square wave


for i in range(len(t)):
    v.append(A*num.sin(2*num.pi*F1*t[i])*u[i])
    


plt.plot(t,u)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Square wave Pulses')
plt.grid(True)
plt.show()

plt.plot(t,x);
plt.xlabel('Time');
plt.ylabel('Amplitude');
plt.title('Carrier');
plt.grid(True)
plt.show()



plt.plot(t,v)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ASK Signal')
plt.grid(True)
plt.show()

'''
sample input ---

Enter the frequency of carrier=10

Enter the frequency of pulse=2
'''
