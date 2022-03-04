def printValues(num):
	for i in range(num):
		yield i**2
		
num=int(input())
for i in printValues(num):
	print(i)

