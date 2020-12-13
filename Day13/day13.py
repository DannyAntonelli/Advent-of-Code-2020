with open("./input.txt", "r", encoding="UTF-8") as fin:
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

# Part two (Implementation of the Chinese remainder theorem)
busses = [bus for bus in lines[1].split(",")]
for i in range(len(busses)):
    if busses[i] != "x":
        busses[i] = int(busses[i])

def moduleInverse(n, m):
    m0 = m
    i = 0
    result = 1

    while(n > 1): 
        quotient = n // m 
        temp = m 
        m = n % m 
        n = temp
        temp = i
        i = result - quotient * i
        result = temp 
 
    if (result < 0): 
        result += m0
    return result

a = []
n = []

for i, bus in enumerate(busses):
    if bus != "x":
        if i == 0:
            n.append(bus)
            a.append(0)
        else:
            remainder = bus - (i % bus)
            n.append(bus)
            a.append(remainder)

product = 1
for bus in n:
    product *= bus

prod = []
for bus in n:
    prod.append(product // bus)

y = []
for i in range(len(prod)):
    y.append(moduleInverse(prod[i], n[i]))

number = 0
for i in range(len(a)):
    number += a[i]*prod[i]*y[i]

while (number > product):
    number -= product
    
print(number)