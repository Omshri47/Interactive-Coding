class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        
        prefix_x = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefix_y = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        ans = 0
        
        for r in range(rows):
            for c in range(cols):
                is_x = 1 if grid[r][c] == 'X' else 0
                is_y = 1 if grid[r][c] == 'Y' else 0
                
                
                prefix_x[r+1][c+1] = is_x + prefix_x[r][c+1] + prefix_x[r+1][c] - prefix_x[r][c]
                prefix_y[r+1][c+1] = is_y + prefix_y[r][c+1] + prefix_y[r+1][c] - prefix_y[r][c]
                
                
                if prefix_x[r+1][c+1] == prefix_y[r+1][c+1] and prefix_x[r+1][c+1] > 0:
                    ans += 1
                    
        return ans