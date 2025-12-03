import math
def endOfDial(sum: int,positive: int):
    times = sum % 100
    print(f"times {times}")
    dial = 100 + (times*positive)
    if(dial > 99):
        dial = dial - 100
    print(f"dial {dial}")
    return dial
    


with open('input.txt', 'r') as f:
    current = 50 
    answer = 0
    for line in f:
        print(f"===={line}====")
        direction = line[0]
        number = int(line[1:])
        if(direction == "L"):
            number = number * -1
        toeval = current + number
        itsPositive = 1
        if(toeval<0):
            itsPositive = -1        

        print(f"toeval {toeval}")
        if(toeval <= 0 and current!=0):
            answer += 1;
        if(toeval >=100 or toeval<=-100):
            # partialSum = current + number
            # print(f"partialSum {partialSum}")
            turns = math.floor(abs(toeval)/100)
            print(f"turns {turns}")
            answer += turns
        current = endOfDial(abs(toeval),itsPositive)
        print(f"current {current}")
        print(f"subans its {answer}")   
        # else:
        #     current = toeval


print(f"ans its {answer}")        