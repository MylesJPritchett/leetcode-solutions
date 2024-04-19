class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == '1':
                           self.dfs(grid, i, k)
                           count += 1
        return count
                    
    def dfs(self, grid, i, k):
        if i<0 or k<0 or i>=len(grid) or k>=len(grid[0]) or grid[i][k] != '1':
            return
        grid[i][k] = '#'
        self.dfs(grid, i+1, k)
        self.dfs(grid, i-1, k)
        self.dfs(grid, i, k+1)
        self.dfs(grid, i, k-1)