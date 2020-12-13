with open("input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

def solve(x, y):
    positionX = 0
    positionY = 0
    counter = 0
    for _ in lines:
        positionX = (positionX + x) % 31
        positionY += y
        if positionY >= len(lines):
            break
        if lines[positionY][positionX] == "#":
            counter += 1
    return counter

# Part one
print(solve(3, 1))

# Part two
print(solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))