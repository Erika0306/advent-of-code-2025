with open("day02/input.txt") as file:
    input = file.read().strip()
total_sum = 0
rango = input.split(",")

for r in rango:
    parts = r.split("-")
    start = int(parts[0])
    end = int(parts[1])

    for number in range(start, end + 1):
        text = str(number)
        length = len(text)
        is_invalid = False
        # Try all 
        for block_size in range(1, length // 2 + 1):
            # Not divisible, skip
            if length % block_size != 0:
                continue
            block = text[:block_size]
            times = length // block_size
            if block * times == text:
                is_invalid = True
                break
        if is_invalid:
            total_sum = total_sum + number
print(total_sum)