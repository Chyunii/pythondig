import math

class Point2D:

    def __init__(self, x, y):
        self.x=x
        self.y=y

p1=Point2D(x=30, y=20)
p2=Point2D(x=60, y=50)


a=p2.x-p1.x
b=p2.y-p1.y

c=math.sqrt(math.pow(a,2)+math.pow(b,2))

print(c)
