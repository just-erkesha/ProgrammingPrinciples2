n = int(input())#input amount of demons
mp = {}
for i in range(n):
    d, w = input().split()#input demon name and demon weakness
    if (w not in mp): #if there is no other same weakness
        mp[w] = int(1)
    else: #else add
        mp[w] = mp[w] + int(1)
m = int(input())#input amount of hunters
for i in range(m):
    h, a, k = input().split()
#input  hunter name, ability, the number of demons a hunter can kill
    if (a in mp): # if ability exists in map
        if (mp[a] > 0): 
            n = max(n - min(mp[a], int(k)), 0)#finds the minimal demons that can be killed by the hunter, and substracts from total number of demons
            if (int(k) > mp[a]): #if number of demons that can be killed more than hunter's ability
                mp[a] = 0#clear the element
            else: 
                mp[a] = mp[a] - int(k)#else find the number of remaining demons
print(f'Demons left: {n}')#number of remaining demons