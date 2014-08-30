from Init import Init
from Classify import GetInputMatrixForClassifier,GetInputLabelForClassifier
from sklearn.svm import SVC
from ICA import ICA

print "Initializing..."
G,unLabeled,trainSet = Init()
print "Finish initialization"

labelList = ['Agents','AI','DB','IR','ML','HCI']

X = GetInputMatrixForClassifier(G,trainSet,labelList,2)
y = GetInputLabelForClassifier(G,trainSet,labelList)
print "Start training classifier..."
clf = SVC()
clf.fit(X,y)
print "Finish traiing"

print "Start ICA"
result = ICA(G,unLabeled,clf,labelList)

print ""
print "Here is the result:"
print result
