from random import randint as rand

def printClean(str) : print(str, end="")

def readIEEE(str):
    number = float(str.split("e")[0])           # extracts number from IEEE
    sign = str.split("e")[1][0]                 # extracts sign from IEEE 
    exponent = float(str.split("e")[1][1:])     # extracts exponent from IEEE
    
    match sign:
        case "+":
            return round((number * (10 ** exponent)), 7)    # calc as negative exponent if sign is -
        case "-":
            return round((number * (10 ** -exponent)), 7)   # calc as positive exponent if sign is +
        
def identifyNumInstances(file):
    f = open(file, "r")     # open file
    cnt = 0                 # set count to 0
    for x in f:             # for line in file
        cnt += 1                # increment counter
    f.close()               # close file
    return cnt              # return count of lines in file

def identifyNumFeatures(file):
    f = open(file, "r")                                         # open file
    line1 = f.readline()                                        # read one line
    featuresList =  [i for i in line1.split(" ") if i != ""]    # splits string into all columns and removes spaces
    featuresList = featuresList[1:]                             # removes the class label
    f.close()                                                   # close file
    return len(featuresList)                                    # return number of features