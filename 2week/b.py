n = int(input())#reads the length of the array
arr = list(map(int, input().split()))

max = arr[0]*arr[1]#take one value as a maximum product
for i in range(n):
	for j in range(n):
		if i == j:
			continue#elements canot be multiplied to itself
		if max<=arr[i]*arr[j]:
			max= arr[i]*arr[j]#maximum product
print(max)