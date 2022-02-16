letters = list(set(input().split()))#inputted text, automatically takes words without spaces
print(len(letters))#shows how many words in total
letters.sort()#sorted words
for i in letters:
    if '.' in i or ',' in i or '?' in i or '!' in i:
        print(i[:-1])#removes a last character, in this case all punctuation marks
    else:
        print(i)