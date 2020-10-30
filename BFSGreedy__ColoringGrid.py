#My idea is that for each final color, compute number of connected components of different colors using BFS and then take the minimum across all final colors.
#O(KNM)
from collections import deque
def bfs(grid, x, y, m, n):
    queue = deque([(x, y)])
    visited = set([(x, y)])
    
    col = grid[x][y]
    
    while len(queue) > 0:
        i, j = queue.popleft()
        
        p = [[-1,0], [0,-1], [1,0], [0,1]]
        for a, b in p:
            if 0 <= i+a < m and 0 <= j+b < n and (i+a, j+b) not in visited and grid[i+a][j+b] == col:
                queue.append((i+a, j+b))
                visited.add((i+a, j+b))
                
    return visited

def coloring_grid(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    m = len(grid)
    n = len(grid[0])
    
    colors = set()
    for i in range(m):
        for j in range(n):
            colors.add(grid[i][j])
    
    min_cnts = float("Inf")
    
    for x in colors:
        visited = set()
        cnts = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != x and (i, j) not in visited:
                    v = bfs(grid, i, j, m, n)
                    visited.update(v)
                    cnts += 1
                    
        min_cnts = min(min_cnts, cnts)
        
    return min_cnts