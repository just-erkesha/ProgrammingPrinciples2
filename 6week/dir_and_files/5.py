array=list(input().split())
with open('int.txt', "w") as myfile:
        for a in array:
                myfile.write("%s\n" % a)