from helper import *

print("\nWelcome to drodr211's Feature Selection Algorithm.\n")

fileName = input("Enter file name:\n\n  >>> ")

# algo = int(input("\nWhich algorithm to use?\n\n    1. Forward Selection\n    2. Backwards Elimination\n\n  >>> "))
numFeatures = identifyNumFeatures(fileName)
numInstances = identifyNumInstances(fileName)

print(f"\nThis dataset has {numFeatures} features with {numInstances} instances.\n")

c = classifier(fileName)

match fileName:
    case "small-test-dataset.txt": 
        print("Testing small dataset with feature set {3,5,7}")
        start = time.perf_counter()
        validator({3,5,7}, c)
        end = time.perf_counter()
        print(f"Done testing in {round(end-start, 3)} seconds")
    case "large-test-dataset.txt": 
        print("Testing large dataset with feature set {1,15,27}")
        start = time.perf_counter()
        validator({1,15,27}, c)
        end = time.perf_counter()
        print(f"Done testing in {round(end-start, 3)} seconds")

print("\n")

# match algo:
#   case 1:
#        forwardSearch(numFeatures)
#    case 2:
#        backwardsElim(numFeatures)