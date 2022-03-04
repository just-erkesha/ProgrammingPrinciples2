def printValues(num):
	for i in range(num, -1, -1):
		yield i
		
num=int(input())
for i in printValues(num):
	print(i)

