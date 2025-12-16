positon = 50 
counter = 0
with open("day01/input.txt") as file:
    for line in file:
        # Line breaks and spaces
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])
        if direction == "L":
            positon -= distance
        else:
            positon += distance
        positon = positon % 100
        if positon == 0:
            counter += 1

print(counter)