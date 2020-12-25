with open("./input.txt", "r", encoding="UTF-8") as fin:
    cups = [int(cup) for cup in fin.read()]

print("Welcome to Day 23!")
print("="*30)

class Cup():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def printCups(self):
        result = ""
        next = self.right

        while next != self:
            result += str(next.value)
            next = next.right

        print(result)

def solve(cups, moves, part):
    cupList = [None] * (len(cups) + 1)

    firstCup = Cup(cups[0])
    current = firstCup
    cupList[current.value] = current

    for num in cups[1:-1]:
        cup = Cup(num)
        current.right = cup
        cup.left = current
        current = cup
        cupList[current.value] = current

    lastCup = Cup(cups[-1])
    lastCup.left = current
    current.right = lastCup
    lastCup.right = firstCup
    firstCup.left = lastCup
    cupList[lastCup.value] = lastCup

    current = firstCup
    for _ in range(moves):
        cup1 = current.right
        cup2 = cup1.right
        cup3 = cup2.right
        pickUp = (cup1.value, cup2.value, cup3.value)

        current.right = cup3.right
        (cup3.right).left = current

        destination = current.value - 1

        found = False
        while not found:
            if destination < 1:
                destination = len(cups)

            if destination not in pickUp:
                newCup = cupList[destination]
                found = True

            destination -= 1

        cup3.right = newCup.right
        (cup3.right).left = cup3
        newCup.right = cup1
        cup1.left = newCup
        current = current.right

    if part == 1:
        print("Solution #1: ", end="")
        cupList[1].printCups()
    else:
        print("Solution #2:", cupList[1].right.value * (cupList[1].right).right.value)

# Part one
solve(cups, 100, 1)

# Part two
for num in range(len(cups) + 1, 1000001):
    cups.append(num)

solve(cups, 10000000, 2)