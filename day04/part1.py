with open("day04/input.txt") as file:
    grid = [line.strip() for line in file]
    rows = len(grid)
    cols = len(grid[0])
    #All 8 
    directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)]
    accessible_rolls = 0 
    #Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            #Check
            if grid[r][c] == '@':
                neighbors = 0
                #Check all 8 directions
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    #Make sure we stay inside the grid
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbors += 1
                #If fewer than 4 
                if neighbors < 4:
                    accessible_rolls += 1
print(accessible_rolls)