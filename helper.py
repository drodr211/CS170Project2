from random import randint as rand
from copy import deepcopy as dcp
import math

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
        for row in range(len(self.instances)):
            for col in range(len(self.instances[row])):
                self.instances[row][col] = readIEEE(self.instances[row][col])
    def normalize(self):
        for col in range(1, self.numFeatures):
            max = self.instances[1][col]
            min = self.instances[1][col]
            for row in range(len(self.instances)):
                data = self.instances[row][col]
                if data > max: max = data
                if data < min: min = data
            for row in range(len(self.instances)):
                self.instances[row][col] = round((self.instances[row][col]-min)/(max-min), 7)   
    def test(self, instance):
        return 0 #label
    
    def __init__(self, filename):
        self.numFeatures = identifyNumFeatures(filename)
        self.instances = []
        f = open(filename)
        for x in f:
            self.instances.append([i for i in x.split(" ") if i != ""])
        f.close()
        self.convertToDecimal()
        self.normalize()
    

def evalFSet(fset): return rand(0,1000) / 10 

def printClean(str) : print(str, end="")

def modifySet(set,i,mod):
    temp = dcp(set)
    if mod: temp.add(i)
    else:   temp.remove(i)
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

def readIEEE(str):
    number = float(str.split("e")[0])           # extracts number from IEEE
    sign = str.split("e")[1][0]                 # extracts sign from IEEE 
    exponent = float(str.split("e")[1][1:])     # extracts exponent from IEEE
    
    match sign:
        case "+":
            return round((number * (10 ** exponent)), 7)
        case "-":
            return round((number * (10 ** -exponent)), 7)
        
def identifyNumInstances(file):
    f = open(file, "r")
    cnt = 0
    for x in f:
        cnt += 1
    f.close()
    return cnt

def identifyNumFeatures(file):
    f = open(file, "r")
    line1 = f.readline()            # read one line
    featuresList =  [i for i in line1.split(" ") if i != ""]  # splits string into all columns and removes spaces
    featuresList = featuresList[1:]          # removes the class id
    f.close()

    return len(featuresList)