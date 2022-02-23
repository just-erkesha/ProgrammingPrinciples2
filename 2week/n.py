arr=[]
while(True):
    n=int(input())
    if(n==0):
        break
    arr.append(n)
for i in range(len(arr)//2):
    print(arr[i]+arr[i*(-1)-1], end=" ")
if len(arr) & 1:# if it'odd
    print(arr[len(arr)//2])#print the central element