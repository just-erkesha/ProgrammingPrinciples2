n=int(input())
li=[]
for txt in range(n):
    txt=str(input())
    if "@gmail.com" in txt:
       li.append(txt.replace("@gmail.com", ""))

for x in li:
  print(x)