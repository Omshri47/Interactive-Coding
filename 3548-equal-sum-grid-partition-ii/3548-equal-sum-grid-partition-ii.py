class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
    
        m, n = len(grid), len(grid[0])
        MAX_VAL = 100000
        
        min_r = [float('inf')] * (MAX_VAL + 1)
        max_r = [-1] * (MAX_VAL + 1)
        min_c = [float('inf')] * (MAX_VAL + 1)
        max_c = [-1] * (MAX_VAL + 1)
        
        row_sum = [0] * m
        col_sum = [0] * n
        total_sum = 0
        
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                row_sum[r] += val
                col_sum[c] += val
                total_sum += val
                
                if min_r[val] == float('inf'): min_r[val] = r
                max_r[val] = max(max_r[val], r)
                if min_c[val] == float('inf'): min_c[val] = c
                max_c[val] = max(max_c[val], c)
                
        def exists(val):
            return val <= MAX_VAL and max_r[val] != -1

        s_top = 0
        for i in range(m - 1):
            s_top += row_sum[i]
            s_bot = total_sum - s_top
            
            if s_top == s_bot:
                return True
                
            elif s_top > s_bot:
                delta = s_top - s_bot
                if exists(delta):
                    if i == 0:
                        if grid[0][0] == delta or grid[0][n-1] == delta: return True
                    elif n == 1:
                        if grid[0][0] == delta or grid[i][0] == delta: return True
                    else:
                        if min_r[delta] <= i: return True
                        
            else: 
                delta = s_bot - s_top
                if exists(delta):
                    if i == m - 2: 
                        if grid[m-1][0] == delta or grid[m-1][n-1] == delta: return True
                    elif n == 1:
                        if grid[i+1][0] == delta or grid[m-1][0] == delta: return True
                    else:
                        if max_r[delta] >= i + 1: return True

        s_left = 0
        for j in range(n - 1):
            s_left += col_sum[j]
            s_right = total_sum - s_left
            
            if s_left == s_right:
                return True
                
            elif s_left > s_right:
                delta = s_left - s_right
                if exists(delta):
                    if j == 0:
                        if grid[0][0] == delta or grid[m-1][0] == delta: return True
                    elif m == 1:
                        if grid[0][0] == delta or grid[0][j] == delta: return True
                    else:
                        if min_c[delta] <= j: return True
                        
            else:
                delta = s_right - s_left
                if exists(delta):
                    if j == n - 2:
                        if grid[0][n-1] == delta or grid[m-1][n-1] == delta: return True
                    elif m == 1:
                        if grid[0][j+1] == delta or grid[0][n-1] == delta: return True
                    else: 
                        if max_c[delta] >= j + 1: return True

        return False