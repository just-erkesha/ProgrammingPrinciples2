class Shape:
 def area():
     print(0)
    
class Square(Shape):
 def init(self, length):
        self.length=length

c = Shape()
s=Square()
l = int.input()
s.init(l)

c.printString()