class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # scan horizontal then vertical
        edges = 0
        for row in grid:
            
            prev = 0
            for col in row:
               
                
                if col != prev:
                    edges += 1
                    prev = col
                    
            if prev == 1:
                edges += 1
       
        
        for i in range(0, len(grid[0])):
            prev = 0
            for k in range(0, len(grid)):
                if grid[k][i] != prev:
                    edges += 1
                    prev = grid[k][i]
            if prev == 1:
                edges += 1
                    
        return edges