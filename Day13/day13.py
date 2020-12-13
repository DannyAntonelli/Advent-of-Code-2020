with open("test.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

# Part one
timestamp = int(lines[0])
busses = [int(num) for num in lines[1].split(",") if num != "x"]
minTime = timestamp
position = 0

for i, bus in enumerate(busses):
    remainder = timestamp % bus

    if remainder == 0:
        waitingTime = 0
    else:
        waitingTime = bus - (remainder)

    if waitingTime < minTime:
        minTime = waitingTime
        position = i

print(minTime * busses[position])

# Part two
busses = [bus for bus in lines[1].split(",")]
for i in range(len(busses)):
    if busses[i] != "x":
        busses[i] = int(busses[i])

