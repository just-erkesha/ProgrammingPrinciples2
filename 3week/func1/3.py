def solve(numheads, numlegs):
    twolegs_total=numheads*2#all two legs rabit and chickens
    half_four_legs= numlegs-twolegs_total#half of four legs
    four_legs=half_four_legs*2
    rabbits= int(four_legs/4)
    chickens=int(numheads-rabbits)
    print("Rabbits:", rabbits, "/n Chickens:", chickens)

solve(35, 94)