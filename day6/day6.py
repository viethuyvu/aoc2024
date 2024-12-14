with open ('input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]

obstacles = []
guard_location = None

for row_index, row in enumerate(grid):
    if '^' in row:
        col_index = row.index('^')
        guard_location = (row_index, col_index)
    if '#' in row:
        for col_index, cell in enumerate(row):
            if cell == '#':
                obstacles.append((row_index, col_index))


def d6p1 (guard_location, obstacles):
    direction = 'up'
    visited = set() #set in python
    while True:
        if direction == 'up':
            new_location = (guard_location[0] - 1, guard_location[1])
        elif direction == 'down':
            new_location = (guard_location[0] + 1, guard_location[1])
        elif direction == 'left':
            new_location = (guard_location[0], guard_location[1] - 1)
        elif direction == 'right':
            new_location = (guard_location[0], guard_location[1] + 1)

        if new_location[0] < 0 or new_location[0] >= len(grid) or new_location[1] < 0 or new_location[1] >= len(grid[0]):
            break

        if new_location in obstacles:
            if direction == 'up':
                direction = 'right'
            elif direction == 'right':
                direction = 'down'
            elif direction == 'down':
                direction = 'left'
            elif direction == 'left':
                direction = 'up'
        else:
            guard_location = new_location
            visited.add(guard_location)
        
    return len(visited)

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def simulate(start_x, start_y, start_dir):
    visited = set()
    x, y, dir = start_x, start_y, start_dir

    while (x, y, dir) not in visited:
        visited.add((x, y, dir))

        # Calculate the new position based on current direction
        new_x = x + directions[dir][0]
        new_y = y + directions[dir][1]

        # Check if the new position is within bounds
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            # If there's an obstruction in front
            if grid[new_x][new_y] == '#':
                dir = (dir + 1) % 4  # Turn right 90 degrees
            else:
                # Move forward
                x = new_x
                y = new_y
        else:
            # Out of bounds, no infinite loop
            return False

    return True  # A cycle is detected

def d6p2(start_x, start_y, start_dir):
    infinite_loops = []
    
    # Try placing an obstruction at every empty space ('.')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                grid[i][j] = '#'  # Place obstruction
                if simulate(start_x, start_y, start_dir):  # Check if it causes a cycle
                    infinite_loops.append((i, j))
                grid[i][j] = '.'  # Remove obstruction

    return len(infinite_loops)

    
if __name__ == '__main__':
    print(d6p1(guard_location, obstacles))
    print(d6p2(guard_location[0], guard_location[1], 0))
