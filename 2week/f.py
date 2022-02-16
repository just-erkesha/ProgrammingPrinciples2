n= int(input())#number of payments made by accounting department 
payment ={}
maxes=[]
#iterate to input key and values into dictionary
for i in range(n):
    data = list(map(str,input().split()))
    surname=data[0]#student’s surname
    money=int(data[1])#amount of payment he/she received
    if surname in payment.keys():
        payment[surname]+=money
    else:
        payment[surname]=money

mx = max(payment.values())
maxes=[k for k, v in payment.items() if v == mx]

sort_arr=list(sorted(payment.keys()))

for i in range(len(sort_arr)):
    if sort_arr[i] in maxes:
        print(sort_arr[i], "is lucky!")
    else:
        needs=mx-(payment[sort_arr[i]])
        print(sort_arr[i], "has to receive", needs, "tenge")
