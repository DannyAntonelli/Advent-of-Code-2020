with open("input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

# Part one
answers1 = set()
sumAnswers = 0
for line in lines:
    if line == "\n":
        sumAnswers += len(answers1)
        answers1 = set()
    else:
        for c in line:
            if c != "\n":
                answers1.add(c)
sumAnswers += len(answers1)
print(sumAnswers)

# Part two
answers2 = []
sumAnswers = 0
num = 0
added = set()
for line in lines:
    if line == "\n":
        for c in answers2:
            if answers2.count(c) == num:
                added.add(c)
        sumAnswers += len(added)
        added = set()
        answers2 = []
        num = 0
    else:
        for c in line:
            if c != "\n":
                answers2.append(c)
        num += 1
for c in answers2:
    if answers2.count(c) == num:
        added.add(c)
sumAnswers += len(added)
print(sumAnswers)