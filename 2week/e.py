from operator import xor

num = list(map(int, input().split()))#read n and x in one line
n=num[0]
if len(num)==1:# if input has only one value, then input it on next line
    num.append(int(input()))
x=num[1]
arr= []#create array,list in python

for i in range(n):
    arr.append(x + 2*i)#formula for elements of an array

xor_value=arr[0]#taking first element as a starting value 
for i in range(1,n):
    xor_value^=arr[i]#calculating xor

print(xor_value)#output
