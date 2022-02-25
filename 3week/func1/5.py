import math

def permutations(a):
    dict={}
    repetition=1
    for i in range(len(a)):
        if a[i] in dict.keys():
            dict[a[i]]+=1
        else:
            dict[a[i]]=1

    for value in dict.values():
      repetition*=math.factorial(value)

    formula= (math.factorial(len(a)) / (repetition))
    print(int(formula))


txt=input()
permutations(txt)