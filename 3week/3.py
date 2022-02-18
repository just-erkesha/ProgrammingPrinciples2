class Shape:
 def area():
     print(0)
    
class Rectangle(Shape):
    def init(self, length, width):
        self.length=length
        self.width=width
    def compute_area(self):
        print(self.length*self.width)

c = Shape()
r=Rectangle()
le = int(input())
wid=int(input())
r.init(le,wid)
r.compute_area()