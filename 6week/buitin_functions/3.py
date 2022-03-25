l=input()

rev="".join(reversed(l))
if l==rev:
    print("palindrome")
else:
    print("no")