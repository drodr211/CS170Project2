import random
print("Hello world")

# placenholder evalution function
def evalFSet():
    return random.randint(0, 100) 

def randPercent():
    return random.randint(0,1000) / 10

def expandChildren():
    return 0

def forwardSearch():
    return 0




print("\nWelcome to drodr211's Feature Selection Algorithm.\n\n")

numFeatures = int(input("Enter total number of features: \n\n  >>> ")) 

algo = int(input("\nWhich algorithm to use?. \n\n    1. Forward Selection\n    2. Backwards Elimination\n\n  >>> "))

print("Beginning Search")


