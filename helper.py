from random import randint as rand
import copy
allFeatures = set()

class FSet():
    def __init__(self, set):
        self.set = set
        self.eval = evalFSet(self.set)
    def __repr__(self):
        if self.set:
            return f"Feature set {self.set} with accuracy {self.eval}%"
        else:
            return f"Empty feature set with accuracy {self.eval}%"
    
def evalFSet(fset): return rand(0,1000) / 10 

def expandFset(fset):
    print("Expanding " , end="")
    print(fset, end="")
    print(". . .\n")
    
    maxChild = fset
    for i in allFeatures:
        if i not in fset.set:
            temp = copy.deepcopy(fset.set)
            temp.add(i)
            newChild = FSet(temp)
            print("    ", end = "")
            print(newChild)
            if newChild.eval > maxChild.eval:
                maxChild = copy.deepcopy(newChild)
    print("\n")
    return maxChild


def reduceFset(fset):
    print("Reducing " , end="")
    print(fset, end="")
    print(". . .\n")

    maxChild = fset



    return 0


def forwardSearch(numFeatures):
    global allFeatures
    allFeatures = set(range(1, numFeatures+1))
    currSet = FSet(set())
    print(f"\nStarting forward Search with empty set and random eval.\n")

    while True:
        newSet = expandFset(currSet)
        if newSet == currSet:
            print(f"=========== SEARCH COMPLETE =========== \n The best is {newSet}\n\n")
            break
        else:
            currSet = newSet
            continue
    return 0

def backwardsElim(numFeatures):
    global allFeatures
    allFeatures = set(range(1, numFeatures+1))


    return 0




