#this file contains functions that implement the ICA collective classification

from Classify import GetFeatureVector


def ICA(G,unLabeled,clf,labelList):
    '''
    Implement ICA(iterative classifing algorithm)
    Input:
    G: graph
    unLabeled: a list of node ID that need to be labeled
    clf: a trained classifier
    labelList: a label list that related each label to a list

    Return:
    a dictionary that contains pairs of nodeID and label result
    '''
    NUM_OF_LOOP = 500

    reval = {}
    for nodeID in unLabeled:
        #first just use neighbors to label
        featureVec = GetFeatureVector(G,nodeID,labelList,1)
        y_index = clf.predict(featureVec)[0]
        label = labelList[y_index]
        G.node[nodeID]['label'] = label
        reval[nodeID] = label

    count = 0;
    flagList = [False]*len(unLabeled)#this list is used to determine weather the label in unLabeled changed or not
    while count<= NUM_OF_LOOP:
        #ICA part
        for nodeID in unLabeled:
            featureVec = GetFeatureVector(G,nodeID,labelList,2)
            y_index = clf.predict(featureVec)[0]
            label = labelList[y_index]
            if label != G.node[nodeID]['label']:
               G.node[nodeID]['label'] = label
               reval[nodeID] = label
               flagList[y_index] = True

        if 0 == flagList.count(False):
            break
        else:
            count = count + 1
            for i in range(len(flagList)):
                flagList[i] = False
    print count
    return reval
