with open("./input.txt", "r", encoding="UTF-8") as fin:
    PUB_KEY1 = int(fin.readline())
    PUB_KEY2 = int(fin.readline())

print("Welcome to Day 25, Happy XMAS!")
print("="*30)

CONST_NUMBER = 20201227
def getLoop(KEY, subjectNumber = 7):
    value = 1
    i = 0

    while value != KEY:
        value *= subjectNumber
        value %= CONST_NUMBER
        i += 1

    return i

def transform(subjectNumber, loopSize):
    value = 1

    for _ in range(loopSize):
        value *= subjectNumber
        value %= CONST_NUMBER

    return value

loopSize = getLoop(PUB_KEY1)
print("Solution:", transform(PUB_KEY2, loopSize))