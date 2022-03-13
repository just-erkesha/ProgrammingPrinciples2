import re

txt = input()
x = re.search("[A-Z]+[a-z]+$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
