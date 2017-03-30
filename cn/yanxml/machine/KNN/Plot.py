from numpy import *
import KNN
import matplotlib
import matplotlib.pyplot as plt
import operator

def drawFirstPlot(group,labels,firstColumn,secondColumn):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(group[:,firstColumn],group[:,secondColumn])
    plt.show()


def drawFirstPlotWithColor(group,labels,firstColumn,secondColumn):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(group[:,firstColumn],group[:,secondColumn],15.0*array(labels),15.0*array(labels))
    plt.show()

