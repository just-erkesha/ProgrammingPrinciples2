import os

path = input("Type path name: ")
#/Applications/docs/lessons/PP2/6week/A.txt
if(os.path.exists(path)):
    os.remove(path)
else:
    print("No such path")
    