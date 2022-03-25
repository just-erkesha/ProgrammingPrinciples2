l= input()
low=0
upp=0
for i in l:
    if i.isupper():
        upp+=1
    else:
        low+=1

print("Lower case: ", low)
print("Upper case: ", upp)
