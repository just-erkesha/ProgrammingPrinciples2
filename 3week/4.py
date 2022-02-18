class Point:

    def __init__(self, x,y):
        self.x=x
        self.y=y

    def show(self):
        print(self.x,self.y)

    def move(self):
        self.x=int(input())
        self.y=int(input())

    def dist(self, p,q):
        self.p=p
        self.q=q
        print(int(sqrt( pow((self.x-p), 2) + pow((self.y - q), 2))))

from math import* 
cor=Point(int(input()), int(input()))
cor.show()
cor.move()
cor.dist(int(input()), int(input()))


