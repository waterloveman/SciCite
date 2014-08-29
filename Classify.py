#This file contains the function related to build and use a classifer


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
