class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        
        # Initialize the result matrix
        p = [[0] * m for _ in range(n)]
        
        # First pass: Calculate prefix products
        pref = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = pref
                # Update prefix for the next cell
                pref = (pref * grid[i][j]) % MOD
                
        # Second pass: Calculate suffix products and multiply with prefixes
        suff = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suff) % MOD
                # Update suffix for the next cell
                suff = (suff * grid[i][j]) % MOD
                
        return p
        