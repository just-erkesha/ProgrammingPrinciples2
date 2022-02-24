def back_to_num(digit):
    d = {'0': 'ZER', '1': 'ONE', '2': 'TWO', '3': 'THR', '4': 'FOU', '5': 'FIV', '6': 'SIX', '7': 'SEV', '8': 'EIG', '9': 'NIN'}
    return d[digit]

def to_let(n):
    s = ''
    for i in str(n):
        s = s + back_to_num(i)
    return s

def to_num(s):
    d = {'ZER': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOU': 4, 'FIV': 5, 'SIX': 6, 'SEV': 7, 'EIG': 8, 'NIN': 9}
    return d[s]

def calc(x, y):
    power_x, power_y = len(x) // 3, len(y) // 3#floor division
    new_x, new_y = 0, 0
    for i in range(power_x - 1, -1, -1):
        new_x = new_x + to_num(x[:3]) * (10 ** i)
        x = x[3:]
    for i in range(power_y - 1, -1, -1):
        new_b = new_b + to_num(y[:3]) * (10 ** i)
        y = y[3:]
    return new_x + new_b

x, y = input().split('+')#Divide input into two sections by sign "+"
print(to_let(calc(x, y)))