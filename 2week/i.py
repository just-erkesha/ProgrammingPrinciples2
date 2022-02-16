n = int(input())#number of operations
arr = []
for i in range(n):
    x = input().split()#list with iputs
    if (len(x) == 2): #if list consisits of two elements:1 TomJ&erry
        arr.append(x[1])#input to the array the name of movie
    else: 
        print(arr[0], end = ' ')#else it takes disk from the begining
        arr.pop(0)