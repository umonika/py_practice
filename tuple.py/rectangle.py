class rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
    def peri(self):
        return 2 * (self.l + self.b)    
r1 = rectangle(4,6)
print("area ",r1.area())
print("perimeter :",r1.peri())