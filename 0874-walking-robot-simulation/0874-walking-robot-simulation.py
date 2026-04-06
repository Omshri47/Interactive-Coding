class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        obstacle_set = {tuple(obs) for obs in obstacles}
        
        x, y = 0, 0
        direction_idx = 0  # 0: North, 1: East, 2: South, 3: West
        max_dist_squared = 0
        
        for cmd in commands:
            if cmd == -1:  # Turn right
                direction_idx = (direction_idx + 1) % 4
            elif cmd == -2:  # Turn left
                direction_idx = (direction_idx + 3) % 4
            else:  
                dx, dy = directions[direction_idx]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    max_dist_squared = max(max_dist_squared, x*x + y*y)
                    
        return max_dist_squared
        