#
from numpy import *
import operator
import Plot as plot
from os import listdir

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

def datingRealClassTest():
    hoRatio = 0.10
    datingDateMat,datingLabels = fileToMatrix('datingTestSet2.txt')
    m = datingDateMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(datingDateMat[i,:],datingDateMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print ("the classifier came back with: %d, the real answer is: %d" % ( classifierResult, datingLabels[i]))
        #print " the classifier came back with: %d,the real answer is: %d" % (classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]): errorCount += 1.0
    print ("the total error rate is: %f" % (errorCount/float(numTestVecs)))

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

def testNum(firstNum,secondNum,k):
    group,labels,labelsForColor = createDataSet()
    classifierResult = classify0([firstNum,secondNum],group,labels,k)
    print(classifierResult)

def testNumWithPlot(firstNum,secondNum,k):
    group,labels,labelsForColor = createDataSet()
    classifierResult = classify0([firstNum,secondNum],group,labels,k)
    newgroup = row_stack((group,[firstNum,secondNum])) 
    tmpArray = [1]
    newlabelsForColor = column_stack((labelsForColor,tmpArray))
    plot.drawFirstPlotWithColor(newgroup,newlabelsForColor,0,1)

# Test Points
def pointsTestDataWithColor():
    group,labels,labelsForColor = createDataSet()
    plot.drawFirstPlotWithColor(group,labelsForColor,0,1)

# File Points
def pointsFileDataWithColor(firstNum,secondNum):
    datingDateMat,datingLabels = fileToMatrix('datingTestSet2.txt')
    normMat,ranges,minValues = autoNorm(datingDateMat)
    plot.drawFirstPlotWithColor(normMat,datingLabels,firstNum,secondNum)

def pointsFileNormDataWithColor(firstNum,secondNum):
    datingDateMat,datingLabels = fileToMatrix('datingTestSet2.txt')
    normMat,ranges,minValues = autoNorm(datingDateMat)
    plot.drawFirstPlotWithColor(normMat,datingLabels,firstNum,secondNum)

def pointsFileNormTestDataWithColor(firstNum,secondNum):
    datingDateMat,datingLabels = fileToMatrix('datingTestSet2.txt')
    normMat,ranges,minValues = autoNorm(datingDateMat)
    hoRatio = 0.10
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    for i in range(numTestVecs):
        datingLabels[i] = 4
    plot.drawFirstPlotWithColor(normMat[0:numTestVecs,:],datingLabels[0:numTestVecs],firstNum,secondNum)

def pointsFileNormAllDataWithColor(firstNum,secondNum):
    datingDateMat,datingLabels = fileToMatrix('datingTestSet2.txt')
    normMat,ranges,minValues = autoNorm(datingDateMat)
    hoRatio = 0.10
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    for i in range(numTestVecs):
        datingLabels[i] = 4
    plot.drawFirstPlotWithColor(normMat[:,:],datingLabels[:],firstNum,secondNum)

# for image
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')        #iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total error rate is: %f" % (errorCount/float(mTest)))



