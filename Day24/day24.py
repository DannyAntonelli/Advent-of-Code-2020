with open("Day24/input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

# Part one
dictionary = {
        "e": (2, 0),
        "se": (1, -1),
        "sw": (-1, -1),
        "w": (-2, 0),
        "nw": (-1, 1),
        "ne": (1, 1)
    }

currentTiles = set()
for line in lines:
    line = line.replace("e", "e,").replace("w", "w,")
    directions = line.split(",")[:-1]

    x, y = 0, 0
    for direction in directions:
        dx, dy = dictionary[direction]
        x += dx
        y += dy

    if (x, y) in currentTiles:
        currentTiles.remove((x, y))
    else:
        currentTiles.add((x, y))

print(len(currentTiles))

# Part two
RANGE_ADJ = {(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)}

for _ in range(100):
    nextTiles = set()
    toCheck = set()

    for (x, y) in currentTiles:
        toCheck.add((x, y))
        for (i, j) in RANGE_ADJ:
            toCheck.add((x + i, y + j))

    for (x, y) in toCheck:
        counter = 0

        for (i, j) in RANGE_ADJ:
            newX = x + i
            newY = y + j

            if (newX, newY) in currentTiles:
                counter += 1

        if (x, y) in currentTiles and not (counter == 0 or counter > 2):
            nextTiles.add((x, y))
        
        if (x, y) not in currentTiles and counter == 2:
            nextTiles.add((x, y))

    currentTiles = nextTiles.copy()

print(len(currentTiles))