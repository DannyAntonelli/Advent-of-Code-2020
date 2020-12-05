with open("input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

# Part one
for i in range(len(lines)):
    num1 = int(lines[i])
    for j in range(i, len(lines)):
        num2 = int(lines[j])
        if num1 + num2 == 2020:
            print(num1 * num2)

#Part two
for i in range(len(lines)):
    num1 = int(lines[i])
    for j in range(i, len(lines)):
        num2 = int(lines[j])
        for k in range(j, len(lines)):
            num3 = int(lines[k])
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
