n,m=map(int,input().split())
primnum=False
if(n>1):
    for i in range(2,n//2+1):
        if(n%i==0):
            primnum=True
            break
        else:
            primnum=False
if (n<500 and not primnum and m%2==0):
     print('Good job!')
else:
     print("Try next time!")