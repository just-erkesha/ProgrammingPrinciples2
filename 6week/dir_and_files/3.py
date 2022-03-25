import os

path = input("Type path name: ")
#/Users/akerke_kaldyoraz/Desktop/untitled folder/int.txt
if(os.path.exists(path)):
    print("Path filename: ", os.path.basename(path))
    print("Path directory: ", os.path.dirname(path))
else:
    print("No such path")