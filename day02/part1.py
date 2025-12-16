with open("day02/input.txt") as file:
    input = file.read().strip() #As if it were text
    total = 0 
    rango = input.split(",")
    for i in rango:
        part = i.split("-")
        start = int(part[0])
        end = int(part[1])

        for number in range(start, end + 1 ):
            text = str(number)
            if len(text) % 2 != 0:
                continue
            half = len(text) // 2
            first_half = text[:half]
            second_half = text[half:]
            if first_half == second_half:
                total = total + number
print(total)