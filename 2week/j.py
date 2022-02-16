def pass_check(s):
    upp=low=num=False#at the begining there is no upper, lower or digits are given
    for i in s:
        if i.isdigit():
            num=True#checks if has a digit, so returns true
        elif i.isupper():
            upp=True#checks if it has a upper letters
        elif i.islower():
            low=True#checks if it has a lower letters
    return num and low and upp
arr=[]#array for 
for i in range(int(input())):
    c=input()#given password
    if pass_check(c) and c not in arr:#both conditions should be true to add strong passwords to the array
        arr.append(c)
print(len(arr), *sorted(arr), sep="\n")#print strong passwords in sorted way