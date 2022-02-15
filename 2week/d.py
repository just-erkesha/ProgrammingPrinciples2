def even(n):# sequence should start from 1 not from empty space
    for i in range(1,n+1):
        for j in range(i):
            print("#", end="")
        for j in range(n-i):
            print(".", end="")
        print()

def odd(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(".", end="")
        for j in range(i):
            print("#", end="")
        
        print()

n=int(input())#input the number
if n%2==0:# check if it is even or odd
    even(n)
else:
    odd(n)


