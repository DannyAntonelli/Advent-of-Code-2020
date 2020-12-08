import re

with open("input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

colors = {}
for line in lines:
    line = line.split("contain")
    bag, insideBag = line[0].strip(), line[1]
    listOfBags = [s.strip() for s in insideBag.split(",")]

    pattern = r"\w+ \w+ [^b]*"
    bag = re.match(pattern, bag).group().strip()
    pattern = r"[0-9] " + pattern
    for i in range(len(listOfBags)):
        if re.search(pattern, listOfBags[i]):
            listOfBags[i] = re.match(pattern, listOfBags[i]).group().strip()
    
    colors[bag] = listOfBags

# Part one
def search(dictionary, key, memo={}):
    if key in memo:
        return memo[key]
    results = []

    for bag in dictionary[key]:
        if bag == "no other bags.":
            memo[key] = False
            return False
        if "shiny gold" in bag:
            memo[key] = True
            return True
        results.append(search(dictionary, bag[2:], memo))
        
    memo[key] = bool(sum(results))
    return memo[key]

counter = 0
for color in colors:
    if search(colors, color):
        counter += 1
print(counter)

# Part two
def count(dictionary, key, memo={}):
    if key in memo:
        return memo[key]
    results = []

    for bag in dictionary[key]:
        if bag == "no other bags.":
            memo[key] = 0
            return 0
        numberOfBags = int(bag[0])*(count(dictionary, bag[2:], memo) + 1)
        results.append(numberOfBags)

    memo[key] = sum(results)
    return memo[key]
    
print(count(colors, "shiny gold"))