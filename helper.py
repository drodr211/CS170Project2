from auxiliary import *
from copy import deepcopy as dcp
import math
import time

allFeatures = set()

class FSet():
    def __init__(self, set):
        self.set = set
        self.eval = evalFSet(self.set)
    def __repr__(self):
        if self.set:    return f"Feature set {self.set} with accuracy {self.eval}%"
        else:           return f"Empty feature set with accuracy {self.eval}%"

class classifier():
    def convertToDecimal(self):
        for row in range(len(self.instances)):                                  # for every row
            for col in range(len(self.instances[row])):                         # for every col 
                self.instances[row][col] = readIEEE(self.instances[row][col])   # convert string data to decimal

    def normalize(self):
        print("Normalizing data . . .")
        start = time.perf_counter()
        for col in range(1, self.numFeatures):              # for every column in the matrix
            max = self.instances[1][col]                    # initialize max
            min = self.instances[1][col]                    # initialize min
            for row in range(len(self.instances)):          # for every row for that column
                data = self.instances[row][col]             # get data at row, col
                if data > max: max = data                   # adjust max
                if data < min: min = data                   # adjust min
            for row in range(len(self.instances)):          # adjust all data in the column
                self.instances[row][col] = round((self.instances[row][col]-min)/(max-min), 7) # normalize data (from 0 to 1)
        end = time.perf_counter()
        print(f"Done normalizing in {round(end-start, 3)} seconds!\n")
       
    def test(self, testInstance):
        label = self.instances[0][0]
        dist = math.dist(self.instances[0][1:], testInstance)
        for row in range(len(self.instances)):
            currDist = math.dist(self.instances[row][1:], testInstance)
            if (currDist < dist):
                dist = currDist
                label = self.instances[row][0]

        return label
    
    def __init__(self, filename=0, data=0):
        if filename is not 0:
            self.numFeatures = identifyNumFeatures(filename)                # calc number of features (num of columns)
            self.instances = []                                             # initialize empty list 
            f = open(filename)                                              # open file
            for x in f:                                                     # for line in file
                self.instances.append([i for i in x.split(" ") if i != ""]) # split line to indiv feature vals and remove spaces
            f.close()
            self.convertToDecimal()                                         # convert string data to decimal
            self.normalize()                                                        # close file
        else:
            self.numFeatures = len(data[1]) - 1
            self.instances = data  

    
def modifySet(set,i,mod):
    temp = dcp(set)
    if mod: temp.add(i)         # add feature to set
    else:   temp.remove(i)      # remove feature from set
    return FSet(temp)

def expandFset(fset):
    printClean("Expanding ")
    printClean(fset)
    print(". . .\n")
    
    maxChild = fset
    for i in allFeatures:
        if i not in fset.set:
            newChild = modifySet(fset.set, i, 1)
            printClean("    ")
            print(newChild)
            if newChild.eval > maxChild.eval:
                maxChild = dcp(newChild)
    print("\n")
    return maxChild

def elimFset(fset):
    printClean("Eliminating ")
    printClean(fset)
    print(". . .\n")

    maxChild = fset
    for i in allFeatures:
        if i in fset.set:
            newChild = modifySet(fset.set, i, 0)
            printClean("    ")
            print(newChild)
            if newChild.eval > maxChild.eval:
                maxChild = dcp(newChild)
    print("\n")
    return maxChild

def forwardSearch(numFeatures):
    global allFeatures
    allFeatures = set(range(1, numFeatures+1))
    currSet = FSet(set())
    print(f"\nStarting Forward Search w/ empty set and random eval.\n")

    iters = 0
    while True:
        newSet = expandFset(currSet)
        iters += 1
        if newSet == currSet:
            print(f"=========== SEARCH COMPLETE =========== \n The best is {newSet}\n")
            break
        else:
            currSet = newSet
            continue
    print(f"Finished in {iters} iterations.\n")
    return 0

def backwardsElim(numFeatures):
    global allFeatures
    allFeatures = set(range(1, numFeatures+1))
    currSet = FSet(allFeatures)
    print(f"\nStarting Backwards Elim. w/ full set and random eval.\n")
    
    iters = 0
    while True:
        newSet = elimFset(currSet)
        iters += 1
        if newSet == currSet:
            print(f"=========== SEARCH COMPLETE =========== \n The best is {newSet}\n")
            break
        else:
            currSet = newSet
            continue

    print(f"Finished in {iters} iterations.\n")
    return 0



def trimFeatures(featureSet, instances):
    newData = dcp(instances)
    for row in range(len(newData)):
        offset = 0
        for column in range(1, len(newData[row])):
            if column not in featureSet:
                newData[row].pop(column-offset)
                offset += 1

    return newData 

def validator(featureSet, cl):
    trimmedFeatureData = trimFeatures(featureSet, cl.instances)
    
    success = 0
    fails = 0

    for row in range(len(trimmedFeatureData)):
        testRow = trimmedFeatureData[row]
        testLabel = testRow[0]

        newTestData = dcp(trimmedFeatureData)
        newTestData.remove(testRow)

        testClsfr = classifier(0, newTestData)

        if testClsfr.test(testRow[1:]) == testLabel:
            success += 1
        else:
            fails += 1

    accuracy = success/(success+fails)
    print(f"Accuracy: {round(accuracy*100, 7)}%")
    return round(accuracy, 7)