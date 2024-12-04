from helper import *

print("\nWelcome to drodr211's Feature Selection Algorithm.\n")

fileName = input("Enter file name:\n\n  >>> ")

algo = int(input("\nWhich algorithm to use?\n\n    1. Forward Selection\n    2. Backwards Elimination\n\n  >>> "))
numFeatures = identifyNumFeatures(fileName)
numInstances = identifyNumInstances(fileName)

print(f"\nThis dataset has {numFeatures} features with {numInstances} instances.")

c = classifier(fileName)

match algo:
    case 1:
        forwardSearch(numFeatures)
    case 2:
        backwardsElim(numFeatures)