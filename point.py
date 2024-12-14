import math

"""
defines a point with x and y coordinates
"""
class Point:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y

    """
    accessor for x variable
    """
    def getX(self):
        return self.x

    """
    accessor for y variable
    """
    def getY(self):
        return self.y

    """
    string override to output to a file better
    """
    def __str__(self):
        return f"({self.x},{self.y})"

"""
Child class of point tht includes angle information
used for the start and end points of the curve
"""
class ControlPoint(Point):
    def __init__(self, x:float, y:float, theta:float):
        super().__init__(x, y)
        self.theta = theta*(math.pi/180)

    """
    accessor for theta variable
    """
    def getTheta(self):
        return self.theta