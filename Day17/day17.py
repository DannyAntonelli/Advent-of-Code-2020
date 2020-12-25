with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()
NUM_CICLES = 6

print("Welcome to Day 17!")
print("="*30)

def checkState(previousCubes, x, y, z, w=0, dim=3):
    RANGE_NUM = range(-1, 2)
    countPositive = 0

    if dim == 4:
        RANGE_W = RANGE_NUM
    else:
        RANGE_W = [0]

    for i in RANGE_NUM:
        for j in RANGE_NUM:
            for k in RANGE_NUM:
                for t in RANGE_W:
                    newX = x + i
                    newY = y + j
                    newZ = z + k
                    newW = w + t
                    
                    if (newX != x or newY != y or newZ != z or newW != w) and (newX, newY, newZ, newW) in previousCubes:
                            countPositive += 1

    if (x, y, z, w) in previousCubes and countPositive == 2 or countPositive == 3:
        return (x, y, z, w)
    elif (x, y, z, w) not in previousCubes and countPositive == 3:
        return (x, y, z, w)

    return None

initialCubes = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            initialCubes.add((x, y, 0, 0))

DIM1 = len(lines) + NUM_CICLES
RANGE1 = range(-DIM1, DIM1)
DIM2 = NUM_CICLES + 1
RANGE2 = range(-DIM2, DIM2)

# Part one
currentCubes = initialCubes.copy()
for _ in range(NUM_CICLES):
    nextCubes = set()
    for x in RANGE1:
        for y in RANGE1:
            for z in RANGE2:
                result = checkState(currentCubes, x, y, z)
                if result != None:
                    nextCubes.add(result)
    currentCubes = nextCubes.copy()

print("Solution #1:", len(currentCubes))

# Part two
currentCubes = initialCubes.copy()
for _ in range(NUM_CICLES):
    nextCubes = set()
    for x in RANGE1:
        for y in RANGE1:
            for z in RANGE2:
                for w in RANGE2:
                    result = checkState(currentCubes, x, y, z, w, 4)
                    if result != None:
                        nextCubes.add(result)
    currentCubes = nextCubes.copy()

print("Solution #2:", len(currentCubes))