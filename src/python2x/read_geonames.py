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

   

try:
    inputFile = sys.argv[1]
except:
    print "Usage:", sys.argv[0], " <file>."
    sys.exit(1)
   
eps = 0.000001
lineCount = 0
with open(inputFile, "r") as fileStream:
    for line in fileStream:
        tokens = line.split('\t')
        lat = float(tokens[4])
        lon = float(tokens[5])
        if (isValidLatitude(lat) and isValidLongitude(lon)):
            pass
        else:
            print "Coordinates are invalid!\t", line
        lineCount = lineCount + 1

print lineCount, "lines read."
        
