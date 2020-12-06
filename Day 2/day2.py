with open("input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

# Part one
counter = 0
for line in lines:
    line = line.split(":")
    rangeNum = line[0].split(" ")[0]
    letter = line[0].split(" ")[1]
    numbers = rangeNum.split("-")
    occurencies = line[1].strip().count(letter)

    if occurencies >= int(numbers[0]) and occurencies <= int(numbers[1]):
        counter += 1
print(counter)

# Part two
counter = 0
for line in lines:
    line = line.split(":")
    rangeNum = line[0].split(" ")[0]
    letter = line[0].split(" ")[1]
    numbers = rangeNum.split("-")
    password = line[1].strip()
    
    if (password[int(numbers[0])-1] == letter) ^ (password[int(numbers[1])-1] == letter):
        counter += 1
print(counter)