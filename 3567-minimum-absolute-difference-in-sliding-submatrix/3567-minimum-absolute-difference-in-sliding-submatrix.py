class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        
        
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                
                
                unique_vals = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        unique_vals.add(grid[x][y])
                
                
                if len(unique_vals) < 2:
                    ans[i][j] = 0
                else:
                    
                    sorted_vals = sorted(list(unique_vals))
                    min_diff = float('inf')
                    
                    for v in range(1, len(sorted_vals)):
                        diff = sorted_vals[v] - sorted_vals[v-1]
                        if diff < min_diff:
                            min_diff = diff
                            
                    ans[i][j] = min_diff
                    
        return ans