class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for r in range(m):
            for c in range(n):
                
                sums.add(grid[r][c])
                
               
                s = 1 
                
                while r + 2 * s < m and c - s >= 0 and c + s < n:
                    current_sum = 0
                    
                    # Top corner to Right corner
                    for i in range(s):
                        current_sum += grid[r + i][c + i]
                    # Right corner to Bottom corner
                    for i in range(s):
                        current_sum += grid[r + s + i][c + s - i]
                    # Bottom corner to Left corner
                    for i in range(s):
                        current_sum += grid[r + 2 * s - i][c - i]
                    # Left corner back to Top corner
                    for i in range(s):
                        current_sum += grid[r + s - i][c - s + i]
                    
                    sums.add(current_sum)
                    s += 1
        
        
        res = sorted(list(sums), reverse=True)
        return res[:3]