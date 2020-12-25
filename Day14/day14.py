with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

print("Welcome to Day 14!")
print("="*30)

def sumMemory(memory):
    sumValues = 0
    for address in memory:
        sumValues += memory[address]
    return sumValues

# Part one
memory = {}
for line in lines:
    line = line.split("=")

    if line[0].strip() == "mask":
        mask = line[1].strip()
    
    else:
        instruction = line[0].split("[")
        instruction[1] = instruction[1].replace("]", "").strip()
        value = bin(int(line[1].strip()))[2:].zfill(36)
        newValue = ""

        for i in range(len(value)):
            if mask[i] == "1":
                newValue += "1"
            elif mask[i] == "0":
                newValue += "0"
            else:
                newValue += value[i]

        memory[instruction[1]] = int(newValue, 2)

print("Solution #1:", sumMemory(memory))

# Part two
memory = {}
for line in lines:
    line = line.split("=")

    if line[0].strip() == "mask":
        mask = line[1].strip()
    
    else:
        instruction = line[0].split("[")
        instruction[1] = instruction[1].replace("]", "").strip()
        instruction[1] = bin(int(instruction[1]))[2:].zfill(36)
        value = int(line[1].strip())

        address = ""
        for i in range(len(instruction[1])):
            if mask[i] == "1":
                address += "1"
            elif mask[i] == "0":
                address += instruction[1][i]
            else:
                address += "X"

        addresses = []
        for i in range(2 ** address.count("X")):
            num = bin(i)[2:].zfill(address.count("X"))
            newAddress = address

            for c in num:
                newAddress = newAddress.replace("X", c, 1)

            addresses.append(newAddress)
        
        if "X" in address:
            for a in addresses:
                memory[a] = value
        else:
            memory[address] = value

print("Solution #2:", sumMemory(memory))