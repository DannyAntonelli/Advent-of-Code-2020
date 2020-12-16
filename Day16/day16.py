with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

stop = lines.index("your ticket:\n") - 1
conditions = {}
for line in lines[:stop]:
    line = line.split(":")
    key = line[0]

    ranges = line[1].split("or")
    range1 = ranges[0].strip().split("-")
    range1 = range(int(range1[0]), int(range1[1]) + 1)
    range2 = ranges[1].strip().split("-")
    range2 = range(int(range2[0]), int(range2[1]) + 1)

    value = set(range1) | set(range2)
    conditions[key] = [value, [0] * stop]

start = lines.index("nearby tickets:\n") + 1
counter = 0
notValid = set()
for i, line in enumerate(lines[start:]):
    line = line.split(",")

    for num in line:
        num = int(num)
        for condition in conditions:
            if num in conditions[condition][0]:
                ok = True
                break
            else:
                ok = False

        if not ok:
            counter += num
            notValid.add(i)
            break

print(counter)

counter = 0
for i, line in enumerate(lines[start:]):
    if i not in notValid:
        line = line.split(",")
        counter += 1

        for j, num in enumerate(line):
            num = int(num)
            for condition in conditions:
                if num in conditions[condition][0]:
                    conditions[condition][1][j] += 1

positions = {}
for condition in conditions:
    for i, num in enumerate(conditions[condition][1]):
        if num == counter:
            if i in positions:
                positions[i].append(condition)
            else:
                positions[i] = [condition]

for i in range(counter):
    for position in positions:
        if len(positions[position]) == 1:
            toDelete = positions[position][0]
            for pos in positions:
                if pos != position and toDelete in positions[pos]:
                    positions[pos].remove(toDelete)

myTicket = []
start, stop = stop + 2, start - 2
for line in lines[start:stop]:
    line = line.split(",")
    for num in line:
        myTicket.append(int(num))

result = 1
for position in positions:
    if "departure" in positions[position][0]:
        result *= myTicket[position]
print(result)