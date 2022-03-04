def printValues(num):
    for i in range(0,num):
        if i%2==0:
            yield i
		
num=int(input())
for i in printValues(num):
	print(i)

