from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot

# define the true objective function
def objectiveOne(x, a, b):
    return a * x + b
def objectiveTwo(x,a,b,c):
    return a * x + b * x**2 + c


class CurveFit():
   
    def FitOne(self):
        # curve fit
        popt, _ = curve_fit(objectiveOne, self.x, self.y)
        # summarize the parameter values
        a, b = popt
        print('y = %.5f * x + %.5f' % (a, b))
        # plot input vs output
        pyplot.scatter(self.x, self.y)
        # define a sequence of inputs between the smallest and largest known inputs
        self.x_line = arange(min(self.x), max(self.x), 1)
        # calculate the output for the range
        self.y_line = objectiveOne(self.x_line, a, b)

    def FitTwo(self):
        # curve fit
        popt, _ = curve_fit(objectiveTwo, self.x, self.y)
        # summarize the parameter values
        a, b, c = popt
        print('y = %.5f * x + %.5f * x^2 + %.5f' % (a, b, c))
        # plot input vs output
        pyplot.scatter(self.x, self.y)
        # define a sequence of inputs between the smallest and largest known inputs
        self.x_line = arange(min(self.x), max(self.x), 1)
        # calculate the output for the range
        self.y_line = objectiveTwo(self.x_line, a, b,c)

    def __init__(self,x,y,degree = 1):
        self.x = x
        self.y = y
        if degree== 1:
            self.FitOne()
        if degree== 2:
            self.FitTwo()