import math#math library for calculation
x1, y1 = map(int, input().split())
n=int(input())
data= dict()
for i in range(n):
    x2, y2 = map(int, input().split())
    dist=int(math.sqrt(abs((x2-x1)**2+(y2-y1)**2)))
    if dist not in data:#if the same key in the dictionary
        data[dist]=[x2, y2]# value equal to list
    else:
        data[dist].append(x2)#else append separately
        data[dist].append(y2)

for key, value in sorted(data.items()):
    if len(value)>2:#if it has more than two values
        for i in range(0, len(value), 2):
            print(value[i], value[i+1])#print two of them
    else:
        print(*data[key])#print value as a list elements


