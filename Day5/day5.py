with open("./input.txt", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()

print("Welcome to Day 5!")
print("="*30)

def seatId(seat):
    seat = seat.replace("F", "0")
    seat = seat.replace("B", "1")
    seat = seat.replace("L", "0")
    seat = seat.replace("R", "1")
    row = int(seat[:7], 2)
    column = int(seat[7:], 2)
    return row * 8 + column

# Part one
print("Solution #1:", max(set(seatId(line) for line in lines)))

# Part two
seats = sorted(list(seatId(line) for line in lines))
for i in range(len(seats) - 1):
    if seats[i] != (seats[i+1] - 1):
        print("Solution #2:", seats[i] + 1)