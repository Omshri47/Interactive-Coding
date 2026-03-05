class Solution(object):
    def maxArea(self, height):
       # 1. Local variable caching (faster lookup than list/attribute)
        left = 0
        right = len(height) - 1
        max_water = 0
        
        # 2. Cache the height list locally
        h = height 
        
        while left < right:
            # 3. Micro-optimization: Manual min/max is sometimes faster 
            # than calling min() or max() functions in Python's loop
            h_left = h[left]
            h_right = h[right]
            
            if h_left < h_right:
                area = h_left * (right - left)
                left += 1
            else:
                area = h_right * (right - left)
                right -= 1
            
            if area > max_water:
                max_water = area
                
            # 4. Skip redundant heights: This is the real "speed hack"
            # If the next line is shorter than the one we just moved from,
            # it cannot possibly form a larger area.
            while left < right and h[left] <= h_left and h_left < h_right:
                left += 1
            while left < right and h[right] <= h_right and h_right <= h_left:
                right -= 1
                
        return max_water