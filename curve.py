import csv
import sys
from point import *
import matplotlib.pyplot as plt
import math

"""
Curve defines a series of points along a path for the robot to follow
It takes two control points and an arbitrary constant as arguments and creates an array of points
First it defines 2 "imaginary" points, 
one is directly in front of the start point
the other is directly behind the end point
how far in front or behind is determined by the difference between the angle at the control point
and the direction between control points
It then uses these 4 points and linear interpolation to to create a Quartic Bezier Curve
Than it creates 1000 points along the curve and returns them
"""
class Curve:
    def __init__(self, startPoint: ControlPoint, endPoint: ControlPoint, distanceConstant: float = 100):
        self.startPoint = startPoint
        self.endPoint = endPoint
        """
        I think there is a way to use the distance between the points and angle to optimize this automatically,
        but I haven't thought of a way to do it for all test cases
        """
        self.distanceConstant = distanceConstant
        """
        Angle from start to end points between 0 and 2pi
        It is only used to determine the angle between the control point angles and the direction between the points
        """
        direction = math.atan2(self.endPoint.getY() - self.startPoint.getY(),
                               self.endPoint.getX() - self.startPoint.getX())
        if direction < 0:
            direction += 2 * math.pi
        """
        The difference between start angle and direction
        The if statement ensures it is between 0 and pi
        this is used to determine the distance between the first imaginary point and the start point
        """
        startAngleDifference = math.fabs(direction - self.startPoint.getTheta())
        if startAngleDifference > math.pi:
            startAngleDifference = 2 * math.pi - startAngleDifference
        """
        the distance between the start point and the first imaginary point
        The greater the distance between the start angle and direction,
        the farther the imaginary point is
        Dividing startAngleDifference by pi gives a value between 1 and 0

        """
        distance1 = self.distanceConstant * (1.1 - (startAngleDifference / math.pi))

        """
        The difference between end angle and direction
        The if statement ensures it is between 0 and pi
        this is used to determine the distance between the second imaginary point and the end point
        """
        endAngleDifference = math.fabs(direction - self.endPoint.getTheta())
        if endAngleDifference > math.pi:
            endAngleDifference = 2 * math.pi - endAngleDifference
        """
        the distance between the second imaginary point and the end point
        The greater the distance between the end angle and direction,
        the farther the imaginary point is
        Dividing endAngleDifference by pi gives a value between 1 and 0
        """
        distance2 = self.distanceConstant * (1.1 - (endAngleDifference / math.pi))

        """
        Defines the imaginary points using the distances determined from angles
        and the angles of the start and end points
        The first point is added because the first needs to be in front of the start point
        the second is subtracted because the second needs to be behind the end point
        """
        pt1 = Point(self.startPoint.getX() + distance1 * math.cos(self.startPoint.getTheta()),
                    self.startPoint.getY() + distance1 *
                    math.sin(self.startPoint.getTheta()))
        pt2 = Point(self.endPoint.getX() - distance2 * math.cos(self.endPoint.getTheta()),
                    self.endPoint.getY() - distance2 *
                    math.sin(self.endPoint.getTheta()))
        """
        defines 1000 points along the curve including start and end points
        t is between 0 and 1 and represents where the point is along the curve
        The two equations are the equations for a quartic Bezier curve,
        which uses linear interpolation to define a curve using 4 points
        This for loop gets a point along the curve and adds it to an array of all points
        points x and y lists are only for plotting the points with matplotlib
        """
        self.points: [Point] = []
        self.pointsX: [float] = []
        self.pointsY: [float] = []
        for i in range(1000):
            t = i / 999
            x = (1 - t) ** 3 * startPoint.getX() + 3 * (1 - t) ** 2 * t * pt1.getX() + 3 * (
                        1 - t) * t ** 2 * pt2.getX() + t ** 3 * endPoint.getX()
            y = (1 - t) ** 3 * startPoint.getY() + 3 * (1 - t) ** 2 * t * pt1.getY() + 3 * (
                        1 - t) * t ** 2 * pt2.getY() + t ** 3 * endPoint.getY()
            self.points.append(Point(x, y).__str__())
            self.pointsX.append(x)
            self.pointsY.append(y)

    """
    Uses matplotlib to draw the path of the robot
    clear any graph that may be loaded already
    places ticks at the edge of each tile
    limits the graph to the size of the field
    draws a line that follows the points
    """
    def drawCurve(self):
        plt.clf()
        #The field for robotics is 12' x 12' with each tile in the field being 2' so each unit is 0.1"
        plt.yticks(range(0, 1440, 240))
        plt.xticks(range(0, 1440, 240))
        plt.xlim(0,1440)
        plt.ylim(0,1440)
        plt.grid(True)
        plt.plot(self.pointsX, self.pointsY)
        plt.show()
        plt.savefig(sys.stdout.buffer)
        sys.stdout.flush()

    """
    outputs the points to a csv file to be uploaded to an SD card and uploaded
    There is no heading on the csv file because there is 1000 points and it is only for the robot to follow
    If the user wants to see the points, the view button on the gui displays a graph that follows the points
    """
    def saveCurve(self):
        with open("curves.csv",'a',newline='') as csvFile:
            csvWriter =csv.writer(csvFile)
            csvWriter.writerow(self.points)