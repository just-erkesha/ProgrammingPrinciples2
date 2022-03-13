import re
txt=input()
res = re.findall('[a-zA-Z][^A-Z]*', txt)
        
print(res)
