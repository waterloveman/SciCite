#This file contains the function related to build and use a classifer

import numpy as np
from sklearn.svm import SVC

def GetFeatureVector(G,nodeID,labelList,flag):
    '''
    Given a graph and a node build the input feature vector by voting scheme.
    The feature vector looks like this:
    
    ************************************************************************
    [0,1,0,1,0,0...0,1|0,2.........1]
    |---self part-----|neighbor part|
    self part: the feature vector of its own node,evert entry has value of 0,1
    neighbor part: the feature of the node's neighbor,every entry is the total 
    number of neighbors that have this specifi label
    ************************************************************************
   
    flag indicate the way you build the vector:
    
    0: just return the self part
    1: return both part, but just consider the neighbors when count the neighbor part
    2: return both part, consider the node and its neighbors

    input:
    the graph G, the nodeID, flag,labelList
    return value:
    an list of featurn value
    '''
    
    reval = G.node[nodeID]['featureVec'][:] #deep copy here
    
    if flag == 0:
        pass

    if flag == 1:
        neighborPart = [0]*len(labelList) # create a list with the same size of label list
        #count neighbor label
        for neighbor in G.neighbors(nodeID):
            label = G.node[neighbor]['label']
            index = labelList.index(label);
            neighborPart[index] = neighborPart[index] + 1;

        reval = reval + neighborPart

    if flag == 2:
        neighborPart = [0]*len(labelList) # create a list with the same size of label list
        #consider the label of its own label
        label = G.node[nodeID]['label']
        index = labelList.index(label)
        neighborPart[index] = neighborPart[index] + 1;

        #count neighbor label
        for neighbor in G.neighbors(nodeID):
            label = G.node[neighbor]['label']
            index = labelList.index(label);
            neighborPart[index] = neighborPart[index] + 1;

        reval = reval + neighborPart

    return reval

def TrainClassifier(X,y):
    '''
    given input data X and label y, train the classifier
    return : the trained classifier object
    '''
    clf = SVC() # you can put any classifier you want here
    clf.fit(X,y)
    return clf

def GetInputMatrixForClassifier(G,nodeList,labelList,flag):
    '''
    Given a graph and a node list, data feature flag, generate a input matrix for the classifier

    return:
    an array of input feature vectors
    '''

    tempList = []
    for node in nodeList:
        featureVec = GetFeatureVector(G,node,labelList,flag)
        tempList.append(featureVec)

    return np.array(tempList)

def GetInputLabelForClassifier(G,nodeList,labelList):
    '''
    Given a list of label, output the relative number of this label
    return:
    an array of input data label
    '''
    
    tempList = []
    for nodeID in nodeList:
        label = G.node[nodeID]['label']
        tempList.append(labelList.index(label))

    return np.array(tempList)


