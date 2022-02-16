def check(a):
    brackets = ['[]', '{}', '()']#array of brackets in various types
    while any(i in a for i in brackets):#checks if any element is true
        for j in brackets:#returns 
            a = a.replace(j, '')#replaces the brackets on the text with empty space
    return not a#which means if a is empty, so not gives opposite true

txt = input()
if check(txt):#so a exists
    print("Yes")
else:#else need complete the signs
    print("No")