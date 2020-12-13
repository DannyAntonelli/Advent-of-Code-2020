with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()
for i in range(len(lines)):
    lines[i] = list(lines[i].strip())

lines2 = [line[:] for line in lines]

def countSeats(matrix):
    counter = 0
    for line in matrix:
        counter += line.count("#")
    return counter

# Part one
def changeState1(seats, newSeats, posY, posX):
    if posY == 0:
        rangeY = range(2)
    elif posY == len(seats) - 1:
        rangeY = range(-1, 1)
    else:
        rangeY = range(-1, 2)

    if posX == 0:
        rangeX = range(2)
    elif posX == len(seats[0]) - 1:
        rangeX = range(-1, 1)
    else:
        rangeX = range(-1, 2)

    if seats[posY][posX] != ".":
        counter = 0

        for i in rangeY:
            for j in rangeX:
                if seats[posY + i][posX + j] == "#":
                    counter += 1
        
        if counter == 0:
            newSeats[posY][posX] = "#"
        elif counter >= 5:
            newSeats[posY][posX] = "L"

seats = []
while seats != lines:
    seats = [line[:] for line in lines]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            changeState1(seats, lines, i, j)

print(countSeats(seats))

# Part Two
def checkRowColumn(seats, posY, posX):
    lenY = len(seats)
    lenX = len(seats[0])

    rangeUp = range(1, posY + 1)
    rangeDown = range(1, lenY - posY)
    rangeLeft = range(1, posX + 1)
    rangeRight = range(1, lenX - posX)

    counter = 0

    for i in rangeUp:
        if seats[posY - i][posX] == "#":
            counter += 1
            break
        if seats[posY - i][posX] == "L":
            break
        
    
    for i in rangeDown:
        if seats[posY + i][posX] == "#":
            counter += 1
            break
        if seats[posY + i][posX] == "L":
            break

    for i in rangeLeft:
        if seats[posY][posX - i] == "#":
            counter += 1
            break
        if seats[posY][posX - i] == "L":
            break

    for i in rangeRight:
        if seats[posY][posX + i] == "#":
            counter += 1
            break
        if seats[posY][posX + i] == "L":
            break

    return counter

def checkDiagonals(seats, posY, posX):
    lenY = len(seats)
    lenX = len(seats[0])

    distance1 = min(posY, posX) + 1
    distance2 = min(posY + 1, lenX - posX)
    distance3 = min(lenY - posY, posX + 1)
    distance4 = min(lenY - posY, lenX - posX)

    rangeUL = range(1, distance1)
    rangeUR = range(1, distance2)
    rangeBL = range(1, distance3)
    rangeBR = range(1, distance4)

    counter = 0

    for i in rangeUL:
        if seats[posY - i][posX - i] == "#":
            counter += 1
            break
        if seats[posY - i][posX - i] == "L":
            break

    for i in rangeUR:
        if seats[posY - i][posX + i] == "#":
            counter += 1
            break
        if seats[posY - i][posX + i] == "L":
            break
    
    for i in rangeBL:
        if seats[posY + i][posX - i] == "#":
            counter += 1
            break
        if seats[posY + i][posX - i] == "L":
            break

    for i in rangeBR:
        if seats[posY + i][posX + i] == "#":
            counter += 1
            break
        if seats[posY + i][posX + i] == "L":
            break
    
    return counter

def changeState2(seats, newSeats, posY, posX):
    if seats[posY][posX] != ".":
        counter = 0

        counter += checkRowColumn(seats, posY, posX)
        counter += checkDiagonals(seats, posY, posX)
        
        if counter == 0:
            newSeats[posY][posX] = "#"
        elif counter >= 5:
            newSeats[posY][posX] = "L"

seats = []
while seats != lines2:
    seats = [line[:] for line in lines2]

    for i in range(len(lines2)):
        for j in range(len(lines2[i])):
            changeState2(seats, lines2, i, j)           

print(countSeats(seats))