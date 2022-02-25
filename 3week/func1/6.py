def rev(a):
    rever=[]
    for i in range(len(a)-1, -1, -1):
        rever.append(a[i])

    print(*rever)



txt=list(map(str, input().split()))
rev(txt)