with open("./input.txt", "r", encoding="UTF-8") as fin:
    numbers = fin.readline().split(",")
    numbers = [int(number) for number in numbers]

previousPos = {}
for i, number in enumerate(numbers[:-1]):
    previousPos[number] = i
initialPos = previousPos.copy()

def solve(numbers, previousPos, stop):
    number = numbers[-1]

    for i in range(len(numbers) - 1, stop - 1):
        position = previousPos.get(number, -1)

        if position == -1:
            previousPos[number] = i
            number = 0
        else:
            previousPos[number] = i
            number = i - position

    return number

# Part one
print(solve(numbers, previousPos, 2020))

#Part two
previousPos = initialPos.copy()
print(solve(numbers, previousPos, 30000000))