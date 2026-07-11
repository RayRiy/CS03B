#################################################
# CS03B - Summer 2026
# Assignment 1 - Question 1
# Student Name: Rayaan Riyaz
# SID: 20691965
#################################################


import math

class Circle:
    def __init__(self, x=0, y=0, radius = 1):
        self.x = x
        self.y = y
        self.radius = radius
    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x
    def getY(self):
        return self.y
    def setY(self, y):
        self.y = y
    def getRadius(self):
        return self.radius
    def setRadius(self, radius):
        self.radius = radius
    def getArea(self):
        return math.pi * self.radius ** 2
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    def containPoint(self, x, y):
        if math.sqrt((x - self.x)**2 + (y - self.y)**2) <= self.radius:
            return True
        else:
            return False
    def containCircle(self, other):
        distance = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        if distance + other.radius <= self.radius:
            return True
        else:
            return False
    def overlaps(self, other):
        distance = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        if distance <= self.radius + other.radius and not self.containCircle(other) and not other.containCircle(self):
            return True
        else:
            return False


def run():
    """
    Students should implement their code for Question 1 inside this function.
    """
    # Testing:

    c1 = Circle(3, 0, 4)
    c2 = Circle(0, 3, 1)
    c3 = Circle(0, 0, 1)
    c4 = Circle(0, 0, 2)
    
    # Area and Perimeter
    print("Circle 1")
    print("Area:", c1.getArea())
    print("Perimeter:", c1.getPerimeter())
    print()
    
    print("Circle 2")
    print("Area:", c2.getArea())
    print("Perimeter:", c2.getPerimeter())
    print()
    
    print("Circle 3")
    print("Area:", c3.getArea())
    print("Perimeter:", c3.getPerimeter())
    print()
    
    print("Circle 4")
    print("Area:", c4.getArea())
    print("Perimeter:", c4.getPerimeter())
    print()
    
    # Contain Point
    print("Circle 1 contains (5,5):", c1.containPoint(5, 5))
    print("Circle 2 contains (5,5):", c2.containPoint(5, 5))
    print("Circle 3 contains (5,5):", c3.containPoint(5, 5))
    print("Circle 4 contains (5,5):", c4.containPoint(5, 5))
    print()
    
    # Contain Circle
    print("Circle 1 contains Circle 2:", c1.containCircle(c2))
    print("Circle 4 contains Circle 1:", c4.containCircle(c1))
    print("Circle 2 contains Circle 3:", c2.containCircle(c3))
    print()
    
    # Overlaps
    print("Circle 1 overlaps Circle 2:", c1.overlaps(c2))
    print("Circle 1 overlaps Circle 3:", c1.overlaps(c3))
    print("Circle 2 overlaps Circle 4:", c2.overlaps(c4))
    

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()