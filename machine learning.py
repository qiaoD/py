#   # machine learning

import csv
import random
import math
import operator

def loadDataset(filename,split,trainingSet=[], testSet=[]):
    with open(filename) as ifile:
        lines = csv.reader(ifile)
        dataset = list(lines)
        # dataset [['5.1', '3.5', '1.4', '0.2', 'Iris-setosa'], ['4.9', '3.0', '1.4', '0.2', 'Iris-setosa'], ...]
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])    # from string to float
            if random.random() < split:
                trainingSet.append(dataset[x])
            else :
                testSet.append(dataset[x])

        #print(trainingSet)
        #print("end")
        #print(testSet)

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes :
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    #print(classVotes.items())
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    #print(sortedVotes)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    corrent = 0
    for x in range(len(testSet)):
        if(testSet[x][-1] == predictions[x]):
            corrent += 1
    return (corrent / float(len(testSet))) * 100.0

def main():

    trainingSet = []
    testSet = []
    split = 0.67

    # get the data
    #
    # You can download the data on 
    # https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
    loadDataset("1.txt", split, trainingSet, testSet)
    print('TrainingSet :' + repr(len(trainingSet)))
    print('TestSet :' + repr(len(testSet)))

    #generate predictions
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        #print("---")

    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy:' + repr(accuracy) + '%')
    

# main()

    
