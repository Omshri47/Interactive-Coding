class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        last1 = [-1] * (n + 1)
        last2 = [-1] * (n + 1)
        
        min_dist = float('inf')
        
        for i, val in enumerate(nums):
            if last2[val] != -1:
                dist = 2 * (i - last2[val])
                if dist < min_dist:
                    min_dist = dist
            
            last2[val] = last1[val]
            last1[val] = i
            
        return min_dist if min_dist != float('inf') else -1
        