class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        MOD = 10**9+7

        p_max = [0]*n
        p_min=[0]*n

        p_max[0]=p_min[0]=grid[0][0]

        for j in range(1,n):
            p_max[j]=p_min[j]=p_max[j-1]*grid[0][j]

        for i in range(1,m):
            c_max=[0]*n
            c_min=[0]*n
            c_max[0]=c_min[0]=p_max[0]*grid[i][0]
            for j in range(1,n):
                b_prev = max(p_max[j],c_max[j-1])
                w_prev=min(p_min[j],c_min[j-1])

                if grid[i][j]<0:
                    c_max[j]=w_prev*grid[i][j]
                    c_min[j]=b_prev*grid[i][j]
                else:
                    c_max[j]=b_prev*grid[i][j]
                    c_min[j]=w_prev*grid[i][j]
            p_max=c_max
            p_min=c_min
        result = p_max[-1]

        if result<0:
            return -1
        return result % MOD
        