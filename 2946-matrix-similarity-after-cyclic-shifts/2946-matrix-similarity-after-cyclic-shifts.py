class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        n = len(mat[0])
        
        # We only care about the effective shifts
        k = k % n 
        
        for row in mat:
            for j in range(n):
                # Check if the current element matches the one 'k' steps away
                if row[j] != row[(j + k) % n]:
                    return False
                    
        return True