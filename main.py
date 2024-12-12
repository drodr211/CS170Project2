import helper as h
import os.path as p
from helper import *

# Results ###########################################################################
#   Group: Daniel Rodriguez, drodr211, Lec001
#       - Small Dataset Results:
#           Forward: Feature Subset: {NULL_SET}, Acc: 75.0%
#           Backward: Feature Subset: {3, 5}, Acc: 92.0%
#       - Large Dataset Results:
#           Forward: Feature Subset: {1,27}, Acc: 95.5%
#           Backward: Feature Subset: {2-7, 9-20, 22-25, 27-40}, Acc: 73.1%
#       - Cleaned Titanic Dataset Results:
#           Forward: Feature Subset: {2}, Acc: 78.01%
#           Backward: Feature Subset: {1, 2, 3, 6}, Acc: 75.21%
#####################################################################################

print("\nWelcome to drodr211's Feature Selection Algorithm.\n")

h.fileName = input("Enter file name:\n\n  >>> ")
if not p.isfile(h.fileName):
    print("\nFile not found or name invalid. Exiting . . . . . .\n")
    exit()
algo = int(input("\nWhich algorithm to use?\n\n    1. Forward Selection\n    2. Backwards Elimination\n\n  >>> "))

numFeatures = identifyNumFeatures(h.fileName)
print(f"\nThis dataset has {numFeatures} features with {identifyNumInstances(h.fileName)} instances.\n")

match algo:
    case 1:
        start = time.perf_counter()
        forwardSearch(numFeatures)
    case 2:
        start = time.perf_counter()
        backwardsElim(numFeatures)
    case _:
        print("Invalid algorithm choice. Exiting . . . . . .\n")
        exit()
end = time.perf_counter()

print(f"Done searching in {round(end-start, 3)} seconds. \n")