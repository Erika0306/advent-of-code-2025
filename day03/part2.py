with open ("day03/input.txt") as file:
    total = 0
    digits = 12
    for line in file:
        line = line.strip()

        stack = []
        digits_remove =len(line) - digits
        for  digit in line:
            #Remove samller digits 
            while stack and digits_remove > 0 and stack[-1] < digit:
                stack.pop()
                digits_remove -= 1
            stack.append(digit)
        # Keep first 12 digits
        number = int("".join(stack[:digits]))
        total += number
print(total)