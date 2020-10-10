from digitalTdigital import plot

print("Enter the size of Encoded Data : ")
size=int(input())
li=[]
print('Enter the binary bits sequnce of length ',size,' bits : \n')
for i in range(size):
    li.append(int(input()))
plot(li)
