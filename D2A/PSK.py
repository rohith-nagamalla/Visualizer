import matplotlib.pyplot as plt
import numpy as num

f1=int(input('Carrier Sine wave frequency ='))
A=2;
siz=int(input('Enter the size of signal='))
t=num.arange(0,siz,0.001)
#print(t)

# f2=int(input('Message frequency ='))
x=A*num.sin(2*num.pi*f1*t)



u=[]#Message signal
b=[]
for i in range(siz+1):
    b.append((i+0.0))
s=1
for i in t: 
    if(i==b[0]):
        b.pop(0)
        s=int(input())
        #print(s,i,b)
    u.append(s)

#print(u)


v=[]#Sine wave multiplied with square wave
for i in range(len(t)):
    if(u[i]==1):
        v.append(A*num.sin(2*num.pi*f1*t[i]))
    else:
        v.append(A*num.sin(2*num.pi*f1*t[i])*-1)


plt.plot(t,x);
plt.xlabel("time");
plt.ylabel("Amplitude");
plt.title("Carrier");
plt.grid(True)
plt.show()

plt.plot(t,u)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.grid(True)
plt.show()

plt.plot(t,v);
#plt.axis([0 1 -6 6]);
plt.xlabel("t");
plt.ylabel("y");
plt.title("PSK");
plt.grid(True)
plt.show()
'''Enter the frequency of carrier=10
Enter the frequency of pulse=2'''




