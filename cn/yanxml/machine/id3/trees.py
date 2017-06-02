#!/usr/bin/python3
#coding=gbk

'''
ID3
@author: sean
@since 2017-05-31
'''

from math import log
import  operator

# 生成测试使用的dataSet
def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels

# 熵 Entropy
# 计算香农熵的公式 返回熵的值
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    # 统计每种特征值出现的次数
    for featVec in dataSet:
        currentLabels = featVec[-1]
        if currentLabels not in labelCounts.keys():
            labelCounts[currentLabels] = 0
        labelCounts[currentLabels] += 1
    shannonEnt = 0.0
    # 根据公式计算香农熵的值
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

# 划分数据集
# 就是将 axis列为value的对象抽取出来 作为一个结果集返回出来
def splitDataSet(dataSet,axis,value):
    resultDataSet=[]
    for featVec in dataSet:
        if featVec[axis] == value:
            # 下面的两步可以合成一步 代码写的略复杂了 这边将第axis 列的值删除了？
            tmpDataSet = featVec[:axis]
            tmpDataSet.extend(featVec[axis+1:])
            resultDataSet.append(tmpDataSet)
    return resultDataSet

# 选择最好的数据集划分方式
def chooseBeastFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1 # 前几列是条件属性 最后一列是决策属性
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0 ; bestFeatures = -1;
    # range(num) 为 [0,1,2,3,...]
    for i in range(numFeatures):
        featList = [example[i]  for example in dataSet ] # for example in dataSet : featList = example[i] 每个样本的第i列都赋值给featList
        uniqueVals = set(featList) # 去除重复的，保留惟一的属性
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeatures = i
    return bestFeatures

# 选举出类别数目 最多的一类(返回 出现次数最多的一类的 类名)
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

# 创建树 （也就是创建一个决策树分类器）(一个分类器？ 每次选取出 样本内 重要度最大的样本 ， 随后根据样本属性类别的可能性 进行分类)
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet ] # 将所有样本的最后一列赋值给 classList对象
    if classList.count(classList[0]) == len(dataSet):
        return classList[0] # 如果所有的类别标签都相同 那么即 不用再继续划分了
    if len(dataSet[0])==1:
        return majorityCnt(dataSet) # 如果 只有一个属性列 那么使用 多数服从少数原则 进行选举
    # 选择出 最重要的属性
    bestFeat = chooseBeastFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    # 构建树的结点 删除已经使用过后的标签
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues) # 通过set函数 保留唯一性
    for value in uniqueVals:
        subLables = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLables)
    return myTree

# 序列化树 将树保存到本地
def storeTree(inputTree,filename):
    import  pickle
    fw = open(filename,'w')
    pickle.dump(inputTree,fw)
    fw.close()

# 读取文件呃你保存的树形结构
def grabTree(filename):
    import  pickle
    fr = open(filename)
    return pickle.load(fr)

# 其实这样写有点问题，那就是当判断 不属于 这个决策树上的时候 ，新的测试样本无返回值
# 但在结点判断顺利的情况下 程序可以照常运行
def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0] # 获取根结点字符串
    secondDict = inputTree[firstStr] # 获取树的根节点
    featIndex = featLabels.index(firstStr) # 获取 字符串属性在测试样本的列号
    for key in secondDict.keys():
        # 判断测试样本 属于 决策树的哪一层
        if key == testVec[featIndex]:
            if type(secondDict[key]).__name__ == 'dist': # 通过判断 其是否为 字典数据类型 判断是否为跟节点 / Java内可以判断 其子树 是否为空进行判断是否为根结点
                channelLabel = classify(secondDict[key],featLabels,testVec)
            else:
               # channelLabel = key
                channelLabel = secondDict[key]
    return channelLabel









