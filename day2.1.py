import math


def findPInvalidId(id:str):
    length = len(id)
    if (length%2 == 0) :
        sliceIndex = math.floor(length/2) #maybe too much
        rigth = id[:sliceIndex]
        left =id[length-sliceIndex:]
        print(f"index: {sliceIndex}, number: {id}, length: {length}, right: {rigth}, left: {left}")
        if(rigth == left):
            return int(id)
    return 0


with open('input.txt', 'r') as f:
    line = f.readline()
    intervals = line.split(",")
    ans = 0
    invalids = []
    for interval in intervals:
        margins = interval.split("-")
        for id in range(int(margins[0]),int(margins[1])+1):
            invalidId =  findPInvalidId(str(id))
            if(invalidId != 0 ):
                invalids.append(invalidId)
            ans+= invalidId
    print(f"sum: {ans}")
    print(f"invalids: {invalids}")
    
