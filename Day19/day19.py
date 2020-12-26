with open("Day19/input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

print("Welcome to Day 19!")
print("="*30)

stop = 0
while ":" in lines[stop]:
    stop += 1

rules = [None] * stop
for line in lines[:stop]:
    line = line.split(":")
    index = int(line[0])
    values = line[1].strip()

    if '"' in values:
        pattern = values.replace('"', "")
    else:
        values = values.split("|")
        pattern = []

        for value in values:
            value = value.split()
            pattern.append([int(num) for num in value])

    rules[index] = pattern

def search(index, word, rules, i):
    matches = []
    if len(word) == i:
        return matches

    pattern = rules[index]
    if pattern == "a" or pattern == "b":
        if word[i] == pattern:
            matches = [i + 1]
        return matches

    for elem in pattern:
        toSearch = [i]

        for subPattern in elem:
            temp = []
            for j in toSearch:
                temp.extend(search(subPattern, word, rules, j))
            toSearch = temp.copy()

        matches.extend(toSearch)

    return matches

def match(rules):
    counter = 0
    for word in lines[stop+1:]:
        lenght = len(word.strip())
        if lenght in search(0, word, rules, 0):
            counter += 1
    
    return counter

# Part one
print("Solution #1:", match(rules))

# Part two
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print("Solution #2:", match(rules))