from math import gcd
with open ('input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()] #make the input a 2d list so that it is muteable

#use dictionary to store antenna locations
antenna_location = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        char = grid[i][j]
        if char != '.':
            if char not in antenna_location:
                antenna_location[char] = []
            antenna_location[char].append((i,j))

def in_bounds(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def d8p1():
    antinodes = set()
    for antenna, locations in antenna_location.items():
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]
                x_diff = abs(x2 - x1)
                y_diff = abs(y2 - y1)

                if x1 > x2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1

                antinode1_x = x1 - x_diff
                antinode2_x = x2 + x_diff
                
                if y1 > y2:
                    antinode1_y = y1 + y_diff
                    antinode2_y = y2 - y_diff
                else:
                    antinode1_y = y1 - y_diff
                    antinode2_y = y2 + y_diff

                if in_bounds(antinode1_x, antinode1_y):
                    antinodes.add((antinode1_x, antinode1_y))
                if in_bounds(antinode2_x, antinode2_y):
                    antinodes.add((antinode2_x, antinode2_y))

    return len(antinodes)

def fineline(x1, y1, x2, y2):
    m = (x2 - x1) / (y2 - y1)
    b = x1 - m * y1
    return m, b

def d8p2():
    antinodes = set()
    for antenna, locations in antenna_location.items():
        for i in range(len(locations)):
            for j in range(i+1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]

                if x1==x2:
                    for k in range(len(grid)):
                        antinodes.add((x1, k))
                        
                    continue

                if y1==y2:
                    for k in range(len(grid[0])):
                        antinodes.add((k, y1))
                    continue

                m, b = fineline(x1, y1, x2, y2)
                for k in range(len(grid)):
                    for l in range(len(grid[k])):
                        if abs(m*l + b - k) < 1e-10:  # Check if point lies on line
                            antinodes.add((k, l))

    return len(antinodes)

if __name__ == '__main__':
    print(d8p1())
    print(d8p2())


