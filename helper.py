from random import randint as rand
from copy import deepcopy as dcp
allFeatures = set()

class FSet():
    def __init__(self, set):
        self.set = set
        self.eval = evalFSet(self.set)
    def __repr__(self):
        if self.set:    return f"Feature set {self.set} with accuracy {self.eval}%"
        else:           return f"Empty feature set with accuracy {self.eval}%"
    
def evalFSet(fset): return rand(0,1000) / 10 


def modifySet(set,i,mod):
    temp = dcp(set)
    if mod: temp.add(i)
    else:   temp.remove(i)
    return FSet(temp)


def expandFset(fset):
    print("Expanding ", end="")
    print(fset, end="")
    print(". . .\n")
    
    maxChild = fset
    for i in allFeatures:
        if i not in fset.set:
            newChild = modifySet(fset.set, i, 1)
            print("    ", end = "")
            print(newChild)
            if newChild.eval > maxChild.eval:
                maxChild = dcp(newChild)
    print("\n")
    return maxChild


def elimFset(fset):
    print("Eliminating ", end="")
    print(fset, end="")
    print(". . .\n")

    maxChild = fset
    for i in allFeatures:
        if i in fset.set:
            newChild = modifySet(fset.set, i, 0)
            print("    ", end = "")
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




