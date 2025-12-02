
with open('input.txt', 'r') as f:
    current = 50 
    answer = 0
    for line in f:
        direction = line[0]
        number = int(line[1:])
        # print(f"direction is {direction} and number is {number}")
        if(direction == "L"):
            number = number * -1
        # print(f"number with symbol {number}")
        current = current + number
        if(current % 100 == 0 ):
            answer +=1          
       

    print(f"ans its {answer}")        