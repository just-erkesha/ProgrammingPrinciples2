s=input()
t=input()
num=""
f=s.find(t)
if (not(f==-1)):
    num+=str(f)
l=s.rfind(t) 
if (not(l==f) and l!=-1):
    num+=" "
    num+=str(l)
if len(num)!=0:
    print (num)
