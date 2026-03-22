class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        n = len(mat)
        
        # Check exactly 4 orientations
        for _ in range(4):
            if mat == target:
                return True
            
            #  1: Transpose the matrix
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            #  2: Reverse every row 
            for i in range(n):
                mat[i].reverse()
                
        return False