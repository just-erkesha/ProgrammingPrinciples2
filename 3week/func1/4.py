import math
def filter_prime(a):
    for i in a:
        c=0
        for j in range(1,i):
            if i%j == 0:
                c+=1
        if c==1:
            print(i)

a = list(map(int, input().split()))
filter_prime(a)

