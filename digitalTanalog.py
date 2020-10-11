from D2A.ASK import ASK
from D2A.PSK import PSK
from D2A.FSK import FSK

import matplotlib.pyplot as plt


def plot2(li):
    t,v = ASK(li)
    plt.plot(t,v)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('ASK Signal')
    plt.grid(True)
    plt.show()


    t,v = FSK(li)
    plt.plot(t,v)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('FSK Signal')
    plt.grid(True)
    plt.show()



    t,v = PSK(li)
    plt.plot(t,v)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('PSK Signal')
    plt.grid(True)
    plt.show()    


# print("Enter the size of Encoded Data : ")
# size=int(input())
# li=[]
# print('Enter the binary bits sequnce of length ',size,' bits : \n')
# for i in range(size):
#     li.append(int(input()))
# plot2(li)    
