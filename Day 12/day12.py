with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

# Part one
coordinatesShip = {"N": 0, "E": 0, "S": 0, "W": 0}
turn = {"N": ["ESW", "WSE"], "E": ["SWN", "NWS"], "S": ["WNE", "ENW"], "W": ["NES", "SEN"]}
direction = "E"

for line in lines:
    if line[0] == "F":
        coordinatesShip[direction] += int(line[1:])
    
    elif line[0] == "N":
        coordinatesShip["N"] += int(line[1:])

    elif line[0] == "E":
        coordinatesShip["E"] += int(line[1:])

    elif line[0] == "S":
        coordinatesShip["S"] += int(line[1:])

    elif line[0] == "W":
        coordinatesShip["W"] += int(line[1:])

    elif line[0] == "R":
        num = int(line[1:]) // 90 - 1
        direction = turn[direction][0][num]

    elif line[0] == "L":
        num = int(line[1:]) // 90 - 1
        direction = turn[direction][1][num]

print(abs(coordinatesShip["N"] - coordinatesShip["S"]) + abs(coordinatesShip["E"] - coordinatesShip["W"]))

# Part two
coordinatesShip = {"N": 0, "E": 0, "S": 0, "W": 0}
coordinatesWaypoint = {"N": 1, "E": 10, "S": 0, "W": 0}
direction = "E"

for line in lines:
    if line[0] == "F":
        for coordinate in coordinatesWaypoint:
            coordinatesShip[coordinate] += int(line[1:]) * coordinatesWaypoint[coordinate]
    
    elif line[0] == "N":
        coordinatesWaypoint["N"] += int(line[1:])

    elif line[0] == "E":
        coordinatesWaypoint["E"] += int(line[1:])

    elif line[0] == "S":
        coordinatesWaypoint["S"] += int(line[1:])

    elif line[0] == "W":
        coordinatesWaypoint["W"] += int(line[1:])

    elif line[0] == "R":
        num = int(line[1:]) // 90 - 1
        temp = {"N": 0, "E": 0, "S": 0, "W": 0}

        for coordinate in coordinatesWaypoint:
            newCoordinate = turn[coordinate][0][num]
            temp[newCoordinate] = coordinatesWaypoint[coordinate]
        
        coordinatesWaypoint = temp.copy()

    elif line[0] == "L":
        num = int(line[1:]) // 90 - 1
        temp = {"N": 0, "E": 0, "S": 0, "W": 0}

        for coordinate in coordinatesWaypoint:
            newCoordinate = turn[coordinate][1][num]
            temp[newCoordinate] = coordinatesWaypoint[coordinate]
        
        coordinatesWaypoint = temp.copy()

print(abs(coordinatesShip["N"] - coordinatesShip["S"]) + abs(coordinatesShip["E"] - coordinatesShip["W"]))