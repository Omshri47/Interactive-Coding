class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]
        
        
        for r in range(m):
        
            sorted_row = sorted(matrix[r], reverse=True)
            
            for i in range(n):
            
                height = sorted_row[i]
                width = i + 1
                
                
                max_area = max(max_area, height * width)
                
        return max_area