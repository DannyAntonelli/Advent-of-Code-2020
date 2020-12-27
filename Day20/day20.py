with open("./input.txt", "r", encoding="UTF-8") as fin:
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

# Part Two TODO
"""
def rotate(tile):
    result = []
    tileReversed = tile[::-1]
    for i in range(len(tile)):
        row = ""
        for line in tileReversed:
            row += line[i]
        result.append(row)

    return result
"""    