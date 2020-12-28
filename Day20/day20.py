with open("Day20/input.txt", "r", encoding="UTF-8") as fin:
    pieces = fin.read().strip().split("\n\n")

print("Welcome to Day 20!")
print("="*30)

tiles = {}
for piece in pieces:
    num, tile = piece.split("\n")[0], piece.split("\n")[1:]
    num = int(num[5:-1])
    tiles[num] = tile

def getSide(tile, coordinate):
    side = ""

    if coordinate == "N":
        side = tile[0]
    elif coordinate == "S":
        side = tile[-1]
    elif coordinate == "E":
        for line in tile:
            side += line[-1]
    elif coordinate == "W":
        for line in tile:
            side += line[0]

    assert coordinate in "NSEW"
    return side

def getCorners(tiles):
    matches = {}
    checked = set()
    coordinates = "NSEW"

    for num1 in tiles:
        for num2 in tiles:

            key = (num1, num2)
            if (key[1], key[0]) in checked:
                continue
            checked.add(key)

            if num1 != num2:

                for c1 in coordinates:
                    for c2 in coordinates:
                        side1 = getSide(tiles[num1], c1)
                        side2 = getSide(tiles[num2], c2)

                        if side1 == side2 or side1 == side2[::-1]:
                            matches[num1] = matches.get(num1, "") + c1
                            matches[num2] = matches.get(num2, "") + c2
    
    corners = {}
    for num in matches:
        if len(matches[num]) == 2:
            corners[num] = matches[num]

    return corners

corners = getCorners(tiles)

# Part one
result = 1
for corner in corners:
    result *= corner
print("Solution #1:", result)

# Part Two
def rotate(tile):
    result = []
    tileReversed = tile[::-1]
    for i in range(len(tile)):
        row = ""
        for line in tileReversed:
            row += line[i]
        result.append(row)

    return result

def rotateAndFlip(tile):
    result = [tile]
    for _ in range(3):
        tile = rotate(tile)
        result.append(tile)
    
    tile = tile[::-1]
    result.append(tile)
    for _ in range(3):
        tile = rotate(tile)
        result.append(tile)

    return result

def stripEdges(tile):
    return [line[1:-1] for line in tile[1:-1]]

def match(tiles, tile1, coordinate1, coordinate2):
    side1 = getSide(tile1, coordinate1)

    for num2 in tiles:
        tile2 = tiles[num2]

        if tile1 != tile2:
            for combination in rotateAndFlip(tile2):
                side2 = getSide(combination, coordinate2)

                if side1 == side2:
                    tiles.pop(num2)
                    return combination

def lineMatch(tiles, tile1, dim):
    yield tile1

    for _ in range(DIM_LINE - 1):
        tile2 = match(tiles, tile1, "E", "W")
        tile1 = tile2
        yield tile1

def getImage(tiles, topLeft, dim):
    firstTile = topLeft
    image = []

    while True:
        imageLine = lineMatch(tiles, firstTile, dim)
        imageLine = [stripEdges(elem) for elem in imageLine]
        image.extend(map("".join, zip(*imageLine)))

        if len(tiles) == 1:
            return image

        firstTile = match(tiles, firstTile, "S", "N")

    return image

def countPattern(image, pattern):
    grid = []

    for i, line in enumerate(pattern):
        for j, elem in enumerate(line):
            if elem == '#':
                grid.append((i, j))

    for img in rotateAndFlip(image):
        counter = 0

        for y in range(len(image) - len(pattern)):
            for x in range(len(image) - len(pattern[0])):
                if all(img[y + dy][x + dx] == '#' for dy, dx in grid):
                    counter += 1

        if counter != 0:
            return counter

PATTERN = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]
DIM_LINE = 12

cornerId, sides = corners.popitem()
topLeft = tiles[cornerId]

if sides in ("NE", "EN"):
    topLeft = rotate(topLeft)
elif sides in ("NW", "WN"):
    topLeft = rotate(rotate(topLeft))
elif sides in ("SW", "WS"):
    topLeft = rotate(rotate(rotate(topLeft)))

image = getImage(tiles, topLeft, DIM_LINE)
numMonsters = countPattern(image, PATTERN)
notMonster = sum(line.count("#") for line in image)
roughness = notMonster - 15 * numMonsters

print("Solution #2:", roughness)