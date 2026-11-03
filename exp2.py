def agent(grid, start, goal):
    visited = set()
    x, y = start

    while (x, y) != goal:
        visited.add((x, y))

        if y+1 < len(grid[0]) and grid[x][y+1] == 0 and (x,y+1) not in visited:
            y += 1
        elif x+1 < len(grid) and grid[x+1][y] == 0 and (x+1,y) not in visited:
            x += 1
        else:
            print("Path blocked!")
            return

        print("Position:", (x, y))

    print("Goal Reached!")

grid = [[0,0,1],
        [1,0,1],
        [0,0,0]]

agent(grid, (0,0), (2,2))