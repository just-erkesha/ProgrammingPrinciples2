import re

txt = input()
x = re.search("^[a-z]+_[a-z]+$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
