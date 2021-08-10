from math import degrees
from numpy import angle, arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
from Fits import *
# define the true objective function
PI = 3.141592653
def objectiveOne(x, a, b):
    return a * x + b

def objectiveTwo(x,a,b,c):
    return a * x + b * x**2 + c

class CurveFit():

    def getParabolicPoints(self,a,b,c):
        x = []
        y = []
        for i in range(600):
            x.append(i+20)
            temp = (int(a * (i-300) + b * (i-300)**2 + c)-240)*-1
            y.append(temp)      
            #y.append(int(((a * (i-300) + b * (i-300)**2 + c)-240)*-1))
        #print("x2="+str(x))
        #print("y2="+str(y))
        return x,y

    def getLimits(self,a,b,c=0):
        x_init = 20
        x_end = 620

        if(self.degree==1):
            self.startpoint = (x_init,int(((a*(-300)+b)-240)*-1))
            self.endpoint = (x_end,int(((a*(300)+b)-240)*-1))
        if(self.degree==2):
            #left = 20
            #top = ((a * (-300) + b * (-300)**2 + c)-240)*-1
            #print(top)
            #widht = 600
            #higher = -a/(2*b)
            #height = abs(((a * (higher) + b * (higher)**2 + c)-240)*-1)
            self.x_parabolic,self.y_parabolic = self.getParabolicPoints(a,b,c)
            

    def FitOne(self):
        # curve fit
        popt, _ = curve_fit(objectiveOne, self.x, self.y)
        # summarize the parameter values
        a, b = popt
        #print('y = %.5f * x + %.5f' % (a, b))
        self.function = str('y = %.5f * x + %.5f' % (a, b))

        self.getLimits(a,b)
        # plot input vs output
        #pyplot.scatter(self.x, self.y)
        # define a sequence of inputs between the smallest and largest known inputs
        self.x_line = arange(min(self.x), max(self.x), 1)
        # calculate the output for the range
        self.y_line = objectiveOne(self.x_line, a, b)

    def FitTwo(self):
        # curve fit
        popt, _ = curve_fit(objectiveTwo, self.x, self.y)
        # summarize the parameter values
        a, b, c = popt
        self.function = str('y = %.5f * x^2 + %.5f * x + %.3f' % (b, a, c))
        self.getLimits(a,b,c)
        #print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
        #print(resp)
        # plot input vs output
        #pyplot.scatter(self.x, self.y)
        # define a sequence of inputs between the smallest and largest known inputs
        self.x_line = arange(min(self.x), max(self.x), 1)
        # calculate the output for the range
        self.y_line = objectiveTwo(self.x_line, a, b,c)

    def __init__(self,x,y,degree = 1):
        self.x = x
        self.y = y
        #print("x="+str(x))
        #print("y="+str(y))
        self.degree = degree
        if degree== 1:
            self.FitOne()
        if degree== 2:
            self.FitTwo()