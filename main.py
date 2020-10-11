from digitalTdigital import plot
from digitalTanalog import plot2
print("1)Unipolar-NRZ 2)NRZ-L 3)NRZ-I 4)Polar-RZ 6)Manchester 7)Dif_Man 8)A-M-I")
print("9)ASK 10)FSK 11)PSK")
print("Choose one of the above options:")
option=int(input())
print("Enter the size of Encoded Data : ")
size=int(input())
li=[]
print('Enter the binary bits sequnce of length ',size,' bits : \n')
for i in range(size):
    li.append(int(input()))
if option<=8:
    plot(li,option)
else:
    plot2(li,option)