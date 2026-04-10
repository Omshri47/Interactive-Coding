class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        indices_map = defaultdict(list)
        
        for i, num in enumerate(nums):
            indices_map[num].append(i)
            
        min_distance = float('inf')
        
        for indices in indices_map.values():
            if len(indices) >= 3:
                for p in range(len(indices) - 2):
                    dist = 2 * (indices[p + 2] - indices[p])
                    min_distance = min(min_distance, dist)
                    
        return min_distance if min_distance != float('inf') else -1
        