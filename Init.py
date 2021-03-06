#Initialize:load data, create graph, get train node list and unlabeled node list

import networkx as nx

def Init(nodeFilePath="../Data/citeseer.content",edgeFilePath="../Data/citeseer.cites"):
    '''
    This function complete the task of loading data, create a undirected graph,
    and get the unLabeled lists and train set list.
    
    return value:
    G,unLabeled,trainSed
    '''
    G = nx.Graph()
    nodeFile = open(nodeFilePath)
    edgeFile = open(edgeFilePath)

    #read the file line by line,each line is a node and consits of ID, features and label
    while 1:
        line = nodeFile.readline()
        if not line:
            break;
        nodeID,feature,nodeLabel = processOneLine(line)
        G.add_node(nodeID,featureVec = feature,label = nodeLabel)
    nodeFile.close()

    #add edge to the graph
    nodes = G.nodes()
    while 1:
        line = edgeFile.readline()
        if not line:
            break;
        nodeID1,nodeID2 = getTwoNode(line)
        if nodeID1 in nodes and nodeID2 in nodes:
            G.add_edge(nodeID1,nodeID2)
    edgeFile.close()
    
    #travese all nodes in the graph and get the unLabeled list and trainSet list
    unLabeled = []
    trainSet = []
   
    for nodeID in nodes:
        if G.node[nodeID]['label'] == '':
            unLabeled.append(nodeID)
        flag = True
        for neighborID in G.neighbors(nodeID):
            if G.node[neighborID]['label'] == '':
                flag = False
                break
        if flag == True and G.node[nodeID]['label'] != '':
            trainSet.append(nodeID)
   
    return G,unLabeled,trainSet

def processOneLine(line):
    '''get a input string line from the data file and then split it into id, feature, label
    
    return value:
    nodeID, feature, nodeLabel
    '''
    results = line.split('\t')
    nodeID = results[0]
    feature = results[1:-1]
    nodeLabel = results[-1][0:-1]
    feature = map(int,feature)
    return nodeID, feature, nodeLabel

def getTwoNode (line):
    '''
    get the two end node of a edge

    return value:
    nodeID1,nodeID2
    '''
    result = line.split('\t')
    nodeID1 = result[0]
    nodeID2 = result[1][0:-1]

    return nodeID1,nodeID2
