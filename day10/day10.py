with open ('input.txt', 'r') as f:
    grid = f.read().splitlines()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Possible directions: up, down, left, right    

def is_valid(x, y, visited, target_num):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == str(target_num)

def find_paths(x,y, visited, current_num, reach_nines):
    if grid[x][y] != str(current_num):
        return 0

    if current_num == 9:
        if (x,y) not in reach_nines:
            reach_nines.add((x,y))
            return 1
        return 0
    
    visited.add((x,y))
    count = 0
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, visited, current_num + 1):
            count += find_paths(new_x, new_y, visited, current_num + 1, reach_nines)
    
    # Backtrack: remove current position from path and visited     
    visited.remove((x,y))
    return count

def d9p1():
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '0':
                reach_nines = set()
                visited = set()
                count = find_paths(i, j, visited, 0, reach_nines)
                res += count
    return res

def find_paths2(x,y, visited, current_num):
    if grid[x][y] != str(current_num):
        return 0

    if current_num == 9:
        return 1
    
    visited.add((x,y))
    count = 0
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, visited, current_num + 1):
            count += find_paths2(new_x, new_y, visited, current_num + 1)
    
    # Backtrack: remove current position from path and visited     
    visited.remove((x,y))
    return count

def d9p2():
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '0':
                reach_nines = set()
                visited = set()
                count = find_paths2(i, j, visited, 0)
                res += count
    return res

if __name__ == '__main__':
    print(d9p1())
    print(d9p2())