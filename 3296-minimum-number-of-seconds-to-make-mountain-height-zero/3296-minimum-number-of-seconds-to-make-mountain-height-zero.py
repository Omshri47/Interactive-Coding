import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def can_reduce(total_time):
            reduced_height = 0
            for w in workerTimes:
            
               
                x = (-1 + math.sqrt(1 + ((8 * total_time) // w))) // 2
                reduced_height += x
                if reduced_height >= mountainHeight:
                    return True
            return False

        # Binary search bounds
        low = 1
        
        fastest_worker = min(workerTimes)
        high = fastest_worker * mountainHeight * (mountainHeight + 1) // 2
        
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
                
        """
        solve w * x(x+1)/2 <= total_time
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        