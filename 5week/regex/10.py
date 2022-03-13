import re

def space(txt):
        res = re.findall('[a-zA-Z][^A-Z]*', txt)
        return ''.join(x.lower()+"_" for x in res)

print(space(input()))