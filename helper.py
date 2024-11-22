from random import randint as rand

allFeatures = set()

class FSet():
    def __init__(self, set):
        self.set = set
        self.eval = evalFSet(self.set)
    def __repr__(self):
        return f"Feature set {self.set} with accuracy {self.eval}%"
    
def evalFSet(fset): return rand(0,1000) / 10 

def expandFset(fset):
    for i in allFeatures:
        print(i)
        if i not in fset.set:
            print(FSet(fset.set|{i}))

    return 0

def forwardSearch(numFeatures):
    global allFeatures
    allFeatures = set(range(1, numFeatures+1))
    print(allFeatures)
    expandFset(FSet(set()))
    return 0

def backwardsElim(numFeatures):
     return 0




