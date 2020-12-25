with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

print("Welcome to Day 22!")
print("="*30)

def countPoints(player):
    result = 0
    for i, num in enumerate(player[::-1], 1):
        result += num * i
    return result

start = lines.index("Player 1:\n") + 1
end = lines.index("Player 2:\n") - 1
p1 = []
p2 = []

for line in lines[start:end]:
    p1.append(int(line))

for line in lines[end+2:]:
    p2.append(int(line))

# Part one
def game1(p1, p2):
    while p1 and p2:
        num1 = p1.pop(0)
        num2 = p2.pop(0)

        if num2 > num1:
            p2.extend([num2, num1])
        else:
            p1.extend([num1, num2])
    
    if p1:
        return p1
    return p2

print("Solution #1:", countPoints(game1(p1.copy(), p2.copy())))

# Part two
def game2(p1, p2):
    memo = set()
    while p1 and p2:
        key = tuple(p1), tuple(p2)
        if key in memo:
            return 1
        memo.add(key)

        num1 = p1.pop(0)
        num2 = p2.pop(0)

        if num1 <= len(p1) and num2 <= len(p2):
            winner = game2(p1[:num1], p2[:num2])
        elif num1 > num2:
            winner = 1
        else:
            winner = 2

        if winner == 1:
            p1.extend([num1, num2])
        else:
            p2.extend([num2, num1])
    
    if p1:
        return 1
    return 2

winner = game2(p1, p2)
if winner == 1:
    player = p1
else:
    player = p2

print("Solution #2:", countPoints(player))