positon = 50 
counter = 0
with open("day01/input.txt") as file:
    for line in file:
        # Line breaks and spaces
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])
        for _ in range(distance):
            if direction == "L":
                positon -= 1
            else:
                positon += 1
            positon = positon % 100

            if positon == 0:
                counter += 1
print(counter)