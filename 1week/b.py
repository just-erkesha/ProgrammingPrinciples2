dish = input()
letter=[] 
letter[:0]=dish 
exec=[]
for i in range(len(letter)):
    exec.append(ord(letter[i]))
    exec = list(set(exec))
resnum=sum(exec) 
if resnum>300:
    print("It is tasty!")
else:
    print("Oh, no!")