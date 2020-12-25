import re

with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()
    
print("Welcome to Day 4!")
print("="*30)

# Part one
counter = 0
valid = 0
isValid = False
for line in lines:
    if line == "\n":
        counter = 0
        isValid = False
        continue
    line = line.split()
    for s in line:
        if s[:3] != "cid":
            counter += 1
    if counter == 7 and not isValid:
        valid += 1
        isValid = True
print("Solution #1:", valid)

# Part two
def check(dictionary):
    if len(dictionary) != 7:
        return False

    c1 = int(dictionary["byr"]) in range(1920, 2003)
    c2 = int(dictionary["iyr"]) in range(2010, 2021)
    c3 = int(dictionary["eyr"]) in range(2020, 2031)
    c4 = re.search("(1([5-8][0-9]|[9][0-3])cm)|((59|6[0-9]|7[0-6])in)", dictionary["hgt"])
    c5 = len(dictionary["hcl"]) == 7 and re.search("#([0-9]|[a-f]){6}", dictionary["hcl"])
    c6 = dictionary["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    c7 = len(dictionary["pid"]) == 9 and re.search("[0-9]{9}", dictionary["pid"])

    if c1 and c2 and c3 and c4 and c5 and c6 and c7:
        return True 
    return False

valid = 0
isValid = False
passport = {}
for line in lines:
    if line == "\n":
        passport = {}
        isValid = False
        continue
    line = line.split()
    for s in line:
        temp = s.split(":")
        if temp[0] != "cid":
            passport[temp[0]] = temp[1]
    if check(passport) and not isValid:
        valid += 1
        isValid = True
print("Solution #2:", valid)