import os
with open('/Applications/docs/lessons/PP2/6week/dir_and_files/1.py', 'r') as f1, open('new.txt', 'x') as f2:
    for i in f1:
        f2.write(i)