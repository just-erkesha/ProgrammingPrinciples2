num=int(input())
z=str(input())
if z =="k":
    prec =int(input())
    num/=1024
    num=round(num, prec)

else:
    num*=1024

print(num)