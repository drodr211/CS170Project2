from helper import *







print("\nWelcome to drodr211's Feature Selection Algorithm.\n\n")

numFeatures = int(input("Enter total number of features: \n\n  >>> ")) 

algo = int(input("\nWhich algorithm to use?. \n\n    1. Forward Selection\n    2. Backwards Elimination\n\n  >>> "))

print("Beginning Search")


match algo:
    case 1:
        forwardSearch(numFeatures)
    case 2:
        backwardsElim(numFeatures)


