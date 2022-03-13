import re

def space(txt):
        res = re.findall('[a-zA-Z][^A-Z]*', txt)
        return ''.join(x+" " for x in res)

print(space(input()))