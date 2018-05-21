from math import pi

class circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return pi    
    def peri(self):
        return 2 * pi * (self.r)  
c1 = circle(2)
print('perimeter is',c1.peri())       