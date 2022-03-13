import re

txt = input()
x = re.search("ab{2,3}", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
