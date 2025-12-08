class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        a = [0]
        
        def dfs(x, y):
            grid[x][y] = 0
            a[0] += 1
            
            for dx, dy in direc:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    dfs(nx, ny)
        
        ma = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                if a[0] > ma:
                    ma = a[0]
                a[0] = 0
        
        return ma
                    
        
        