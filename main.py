import helper as h
import os.path as p
from helper import *

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