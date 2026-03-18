class Solution(object):
    def countSubmatrices(self, grid, k):
      
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        dp = [[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                current_val = grid[r][c]
                top = dp[r-1][c] if r>0 else 0
                left = dp[r][c-1] if c>0 else 0
                top_left = dp[r-1][c-1] if(r>0 and c>0)else 0

                total_sum = current_val + top + left - top_left
                dp[r][c]=total_sum

                if total_sum <=k:
                    ans += 1
                else:
                    break
        return ans