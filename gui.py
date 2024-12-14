from tkinter import *
from curve import *
from point import *

"""
gui
inputs 6 values, start x, y, and angle, and end x, y, and angle
one Frame that inputs a value between 1 and 500 defaults to 250
two buttons, one calls a function to draw the graph,
the other saves the graph to a csv file
both test the values to make sure they are acceptable
"""
class Gui:
    def __init__(self,window:Tk):
        self.c1 = None
        self.window = window

        """
        Initial Point Inputs
        """
        self.inputFrame = Frame(self.window)

        self.startFrame = Frame(self.inputFrame)
        self.startLabelFrame = Frame(self.startFrame)
        self.startInputFrame = Frame(self.startFrame)
        self.startXLabel = Label(self.startLabelFrame, text="Start x position")
        self.inputStartX = Entry(self.startInputFrame,width=10)
        self.startYLabel = Label(self.startLabelFrame, text="Start y position")
        self.inputStartY = Entry(self.startInputFrame,width=10)
        self.startAngleLabel = Label(self.startLabelFrame,text="Start angle")
        self.inputStartAngle = Entry(self.startInputFrame,width=10)
        self.startXLabel.pack(side="top")
        self.inputStartX.pack(side="top")
        self.startYLabel.pack(side="top")
        self.inputStartY.pack(side="top")
        self.startAngleLabel.pack(side="top")
        self.inputStartAngle.pack(side="top")
        self.startLabelFrame.pack(side="left")
        self.startInputFrame.pack(side="left")
        self.startFrame.pack(padx=10,pady=10,side="left")

        """
        End Point Inputs
        """
        self.endFrame = Frame(self.inputFrame)
        self.endLabelFrame = Frame(self.endFrame)
        self.endInputFrame = Frame(self.endFrame)
        self.endXLabel = Label(self.endLabelFrame, text="End x position")
        self.inputEndX = Entry(self.endInputFrame, width=10)
        self.endYLabel = Label(self.endLabelFrame, text="End y position")
        self.inputEndY = Entry(self.endInputFrame, width=10)
        self.endAngleLabel = Label(self.endLabelFrame, text="End angle")
        self.inputEndAngle = Entry(self.endInputFrame, width=10)
        self.endXLabel.pack(side="top")
        self.inputEndX.pack(side="top")
        self.endYLabel.pack(side="top")
        self.inputEndY.pack(side="top")
        self.endAngleLabel.pack(side="top")
        self.inputEndAngle.pack(side="top")
        self.endInputFrame.pack(side="right")
        self.endLabelFrame.pack(side="right")
        self.endFrame.pack(anchor='n', padx=10, pady=10, side="right")

        self.inputFrame.pack(side="top")
        """
        Buttons
        """
        self.buttonFrame = Frame(self.window)
        self.viewButton = Button(self.buttonFrame,text="View",command=self.viewGraph)
        self.saveButton = Button(self.buttonFrame,text="Save",command=self.saveGraph)
        self.viewButton.pack(side="left")
        self.saveButton.pack(side="left")
        self.buttonFrame.pack(pady=10,side="bottom")
        """
        Slider
        """
        self.sliderFrame = Frame(self.window)
        self.sliderLabel = Label(self.sliderFrame,text="Distance constant")
        self.slider = Scale(self.sliderFrame,from_=1,to=500,orient="horizontal",length=250)
        self.slider.set(250)
        self.slider.pack(side="top")
        self.sliderLabel.pack(side="top")
        self.sliderFrame.pack(side="top")

        self.errorLabel = Label(text="")
        self.errorLabel.pack(pady= 10,side="top")


    """
    tests the coordinate values to make sure they are between 0 and 1440
    uses modulo to keep the angles between 0 and 360
    if everything is good, it makes a curve object and returns true,
    otherwise it tells the user what went wrong and returns false
    This function is called by both save and draw functions.
    """
    def makeCurve(self):
        x1 = 0
        y1 = 0
        a1 = 0
        x2 = 0
        y2 = 0
        a2 = 0
        try:
            x1 = float(self.inputStartX.get().strip())
            y1 = float(self.inputStartY.get().strip())
            a1 = float(self.inputStartAngle.get().strip())
            x2 = float(self.inputEndX.get().strip())
            y2 = float(self.inputEndY.get().strip())
            a2 = float(self.inputEndAngle.get().strip())
        except:
            self.errorLabel.config(text="Inputs must be numbers")
            return False
        if 0>x1 or 0>y1 or 0>x2 or 0>y2 or 1440<x1 or 1440<y1 or 1440<x2 or 1440<y2:
            self.errorLabel.config(text="Inputs must be between 0 and 1440")
            return False
        a1=a1 % 360
        a2=a2 % 360
        p1 = ControlPoint(x1,y1,a1)
        p2 = ControlPoint(x2,y2,a2)
        self.c1 = Curve(p1, p2, self.slider.get())
        return True

    """
    calls make curve to test values and make the curve, if it returns true,
    it calls draw curve from curve.py to draw it with matplotlib
    """
    def viewGraph(self):
        if self.makeCurve():
            self.c1.drawCurve()

    """
    calls make curve to test values and make the curve, if it returns true,
    it calls save curve from curve.py to output it to a csv file
    """
    def saveGraph(self):
        if self.makeCurve():
            self.c1.saveCurve()