import math


def findDivisors(number: int):
    sqr = math.floor(math.sqrt(number))
    divisors = [1]
    for index in range(2, sqr + 1):
        if number % index == 0:
            divisors.append(index)
            q = int(number / index)
            if q != index:
                divisors.append(q)
    return divisors


def findPInvalidId(id: str):
    if len(id) == 1:
        return False
    divisors = findDivisors(len(id))
    for divisor in reversed(divisors):
        print(f"divisor: {divisor}")
        pattern = id[0:divisor]
        times = int(len(id) / divisor)
        invalidId = True
        for index in range(1, times):
            startIndex = index * divisor
            toCompare = id[startIndex : startIndex + divisor]
            print(f"pattern: {pattern}, toCompare: {toCompare}")
            if pattern != toCompare:
                invalidId = False
                break
        if invalidId:
            return True


with open("input.txt", "r") as f:
    line = f.readline()
    intervals = line.split(",")
    ans = 0
    invalids = []
    fileout = open("output.txt", "w")
    for interval in intervals:
        margins = interval.split("-")
        for id in range(int(margins[0]), int(margins[1]) + 1):
            invalidId = findPInvalidId(str(id))
            if invalidId:
                print(f"==============Invalid id: {id}============")
                print(f"{id}", file=fileout)
                ans += int(id)
    fileout.close()
    print(f"answer:{ans}")
