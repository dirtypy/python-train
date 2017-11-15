#!/usr/bin/python3
#coding=gbk

'''
naive bayes ?朴素贝叶斯
@author: sean
@since 2017-05-31
'''

from imp import reload

from numpy import *

# 数据准备函数
def loadDataSet():
    postingList=[
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]
    classVec=[0,1,0,1,0,1] # 0 标示 无侮辱性言论 1 标示 含侮辱性言论
    return postingList,classVec

# 从样本内归纳字典 （字典内的单词不重复）
def createVocabList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)
    # return vocabSet

# 标识单词出现的次数
def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
            # returnVec[vocabList.index(word)]=1
        else: print "the word : %s is not in my Vocabulary! " %word
    return returnVec

# 朴素贝叶斯 训练函数
# p0Vec p1Vec 是 非侮辱单词向量 / 侮辱单词向量 pAbusive 样本是侮辱性样本的概率
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix) # 获取样本个数
    numWords = len(trainMatrix[0]) # 因为trainMatrix 内是 词向量 所以 维度都是一样的
    pAbusive = sum(trainCategory)/float(numTrainDocs) # sum([1,0])/len([1,0])  1/2 就是文档内包含侮辱单词的概率
    p0Num = zeros(numWords); p1Num = zeros(numWords)
    p0Denom = 0.0 ; p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1 :
            p1Num += trainMatrix[i] # 向量相加
            p1Denom += sum(trainMatrix[i]) # 记录包含的单词个数
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vec = p1Num/p1Denom
    p0Vec = p0Num/p0Denom
    return p0Vec,p1Vec,pAbusive


