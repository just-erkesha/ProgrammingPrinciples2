a = [] 
while  True: 
    n = input() 
    if  n=="0": #zero stops the input of dates
        break 
    a.append(n) 
 
for i in range(len(a)): 
    a[i].reverse() 
#reverse in order to sort array by years, month, dates order
 
a.sort() 
 
for i in range(len(a)): 
    a[i].reverse() 
 #dd, mm, yyyy
for i in range(len(a)): 
    for j in range(3): 
        print(a[i][j], end = ' ') 
    print()#print each element with space