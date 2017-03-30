#
from numpy import *
import operator

# for create the date
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    labelsForColor = [1,1,2,2]
    return group,labels,labelsForColor 

def classify0(inX, dataSet, labels,k): 
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDisIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDisIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
       # sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
        sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

def fileToMatrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append((int(listFromLine[-1]))) # ‘-1’ is 4 in this file
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minValue = dataSet.min(0)
    maxValue = dataSet.max(0)
    ranges = maxValue - minValue;
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minValue,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minValue

def datingClassTest():
    hoRatio = 0.10
    datingDateMat,datingLabels = fileToMatrix('datingTestSet2.txt')
    normMat,ranges,minValues = autoNorm(datingDateMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print ("the classifier came back with: %d, the real answer is: %d" % ( classifierResult, datingLabels[i]))
        #print " the classifier came back with: %d,the real answer is: %d" % (classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]): errorCount += 1.0
    print ("the total error rate is: %f" % (errorCount/float(numTestVecs)))