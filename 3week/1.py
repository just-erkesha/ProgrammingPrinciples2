class MyClass:

    def getString(self,param):
        self.str = param

    def printString(self):

        print(self.str.upper())




c = MyClass()
str = input("Enter string:")
c.getString(str)

c.printString()