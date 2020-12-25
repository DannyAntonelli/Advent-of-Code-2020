with open("./input.txt", "r", encoding="UTF-8") as fin:
    numbers = [int(line) for line in fin]

print("Welcome to Day 9!")
print("="*30)

# Part one
def isWrong(numbers, target):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return False
    return True

for i in range(25, len(numbers)):
    if isWrong(numbers[(i-25):i], numbers[i]):
        position = i
print("Solution #1:", numbers[position])

# Part two
for i in range(position):
    for j in range(i, position):
        if sum(numbers[i:j]) == numbers[position]:
            minNum = min(numbers[i:j])
            maxNum = max(numbers[i:j])
            print("Solution #2:", minNum + maxNum)
            break
