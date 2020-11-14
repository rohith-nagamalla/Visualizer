from digitalTdigital import plot
from digitalTanalog import plot2
print("1)Unipolar-NRZ 2)NRZ-L 3)NRZ-I 4)Polar-RZ 5)Manchester 6)Dif_Man 7)A-M-I 8)Pseudoternary")
print("9)ASK 10)FSK 11)PSK")
print("Choose one of the above options:")
option=int(input())
print("Enter the size of Encoded Data : ")
size=int(input())
li=[]
print('Enter the binary bits sequnce of length ',size,' bits : (enter the bits of the digital signal as a string)')
temp=input()
while not len(temp)==size:
    print('Enter a valid input:')
    temp=input()
for i in range(size):
    li.append(int(temp[i]))
if option<=8:
    plot(li,option)
else:
    plot2(li,option)