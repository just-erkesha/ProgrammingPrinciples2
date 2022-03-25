
# Opening a file
file = open("/Users/akerke_kaldyoraz/Desktop/untitled folder/int.txt","r")
cnt = 0
# Reading from file
content = file.read()
clist = content.split("\n")

for i in clist:
	if i:
		cnt += 1
		
print("Number of lines in the file: ", cnt)
