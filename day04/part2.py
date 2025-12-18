with open("day04/input.txt") as file:
    grid = [list(line.strip()) for line in file]

rows = len(grid)
cols = len(grid[0])

# All 8 directions
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]
total_removed = 0
while True:
    to_remove = []
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                neighbors = 0
                # Check all 8 directions
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # Stay inside the grid
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbors += 1
                # Accessible if fewer than 4 neighbors
                if neighbors < 4:
                    to_remove.append((r, c))
    # Stop
    if not to_remove:
        break
    # Remove all marked rolls
    for r, c in to_remove:
        grid[r][c] = '.'
    total_removed += len(to_remove)

print(total_removed)
