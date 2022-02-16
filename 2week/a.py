arr=list(map(int, input().split()))#read one line numbers and add them to the list
pos=0
result=True

for cnt, val in enumerate(arr):
	pos=max(pos-1, val)#gives the number of max steps to the element on the array
	if pos<=0:#if the steps are negative or ended up
		if cnt!=len(arr)-1:#if the counter does not reach to the last element
			result=False#then result is false
		break#else it can reach, so we stop the loop
if result:#result shows appropriate answer
	print(1)
else:
	print(0)