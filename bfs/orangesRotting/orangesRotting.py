def orangesRotting(grid):

    
    stack = []
    rs,cs = len(grid),len(grid[0])

    def posGenerator(r,c):
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for dr, dc in dirs:
            nr,nc = r+dr,c+dc
            if 0 <= nr < rs and 0 <= nc < cs:
                yield (nr,nc)
        pass
    
    for r in range(rs):
        for c in range(cs):
            if grid[r][c] == 2 and len(stack) < 1:
                stack.append(((r, c), 0))
        pass

    maxDist = 0
    while stack:
        (r, c), d = stack.pop(0)
        maxDist = max(maxDist, d)
        for nr, nc in posGenerator(r, c):
            if grid[nr][nc] == 1:
                stack.append(( (nr, nc), d+1))
                grid[nr][nc] = 2

    for r in range(rs):
        for c in range(cs):
            if grid[r][c] == 1:
                return -1
        pass                
    return maxDist


grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))

