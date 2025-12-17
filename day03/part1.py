with open("day03/input.txt") as file:
    total = 0
    for line in file:
        line=line.strip()
        max_joltage = 0
        # Pick the first digit
        for i in range(len(line)):
            # Pick the second digit
            for j in range(i + 1, len(line)):
                joltage = int(line[i] + line[j])
                if joltage > max_joltage:
                    max_joltage = joltage
        total += max_joltage

print(total)