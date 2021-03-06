#from numpy import *
#import scitools.filetable
import sys

def isValidLatitude(lat):
    """
    Validates the latitude value.
    lat -- the latitude coordinate
    """
    eps = 0.000001
    if (-90 - eps < lat) and (lat < 90 + eps):
        return True
    
    return False

def isValidLongitude(lon):
    """
    Validates the longitude value.
    lon -- the longitude value.
    """
    eps = 0.000001
    if (-180 - eps < lon) and (lon < 180 + eps):
        return True

    return False

def readLines(inputFile, inMemory):
    lineCount = 0
    x = []
    y = []
    with open(inputFile, "r") as fileStream:
        for line in fileStream:
            tokens = line.split('\t')
            lat = float(tokens[4])
            lon = float(tokens[5])
            if (isValidLatitude(lat) and isValidLongitude(lon)):
                if inMemory:
                    x.append(lon)
                    y.append(lat)    
            else:
                print "Coordinates are invalid!\t", line
            lineCount = lineCount + 1

    print lineCount, "lines read."
    if inMemory:
        print len(x), "coordinates read."
 
   

try:
    inputFile = sys.argv[1]
except:
    print "Usage:", sys.argv[0], " <file>."
    sys.exit(1)

inMemory = False
if 2 < len(sys.argv):
    if "in-memory" == sys.argv[2]:
        inMemory = True

readLines(inputFile, inMemory)   
        
