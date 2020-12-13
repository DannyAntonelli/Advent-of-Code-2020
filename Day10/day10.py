with open("input.txt", "r", encoding="UTF-8") as fin:
    numbers = sorted([int(line) for line in fin])
numbers.insert(0, 0)
numbers.append(max(numbers) + 3)

# Part one
diff1 = 0
diff3 = 0

for i in range(len(numbers) - 1):
    difference = numbers[i+1] - numbers[i]

    if difference == 1:
        diff1 += 1
    elif difference == 3:
        diff3 += 1

print(diff1 * diff3)

# Part two
def check(adapters, position=0, checked={}):
    if position in checked:
        return checked[position]
    if position == len(numbers) - 1:
        checked[position] = 1
        return 1

    result = 0
    for secondPosition in range(position + 1, len(numbers)):
        difference = adapters[secondPosition] - adapters[position]

        if difference <= 3:
            resultSubLists = check(adapters, secondPosition, checked)
            result += resultSubLists
    
    checked[position] = result
    return result

print(check(numbers))