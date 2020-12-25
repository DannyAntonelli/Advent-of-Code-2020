with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

print("Welcome to Day 8!")
print("="*30)

def haltingMachine(lines, accumulator, instruction, runned):
    if instruction == len(lines) or runned[instruction]:
        return accumulator, instruction
    runned[instruction] = True

    if lines[instruction][:3] == "acc":
        accumulator += int(lines[instruction][4:])
        instruction += 1
    elif lines[instruction][:3] == "jmp":
        instruction += int(lines[instruction][4:])
    else:
        instruction += 1
    return haltingMachine(lines, accumulator, instruction, runned)

# Part 1
print("Solution #1:", haltingMachine(lines, 0, 0, [False]*len(lines))[0])

# Part 2
for i, line in enumerate(lines):
    newProgram = lines.copy()
    if line[:3] == "nop":
        newProgram[i] = line.replace("nop", "jmp")
    elif line[:3] == "jmp":
        newProgram[i] = line.replace("jmp", "nop")
    else:
        continue

    accumulator, instruction = haltingMachine(newProgram, 0, 0, [False]*len(lines))
    if instruction == len(lines):
        print("Solution #2:", accumulator)