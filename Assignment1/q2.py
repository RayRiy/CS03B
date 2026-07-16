#################################################
# CS03B - Summer 2026
# Assignment 1 - Question 2
# Student Name: Rayaan Riyaz
# SID: 20691965
#################################################


import math

class Triangle:
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def getArea(self):
        s = self.getPerimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def toString(self):
        return f"Triangle: side1 = {self.side1}, side2 = {self.side2}, side3 = {self.side3}"

def run():
    """
    Students should implement their code for Question 2 inside this function.
    """
    #Testing
    
    t1 = Triangle(3, 4, 5)
    print("Triangle 1:")
    print(t1.toString())
    print("Perimeter:", t1.getPerimeter())
    print("Area:", t1.getArea())
    print()
    print("Triangle 2:")
    t2 = Triangle(2, 7, 8)
    print(t2.toString())
    print("Perimeter:", t2.getPerimeter())
    print("Area:", t2.getArea())

    # Example logic:
    # result = 5 + 5
    # print(f"Result: {result}")

if __name__ == "__main__":
    # This allows students to run this specific file 
    # individually for testing (e.g., `python q1.py`)
    run()
