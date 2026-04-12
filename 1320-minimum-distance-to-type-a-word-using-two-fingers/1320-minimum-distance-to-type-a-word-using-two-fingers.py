class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        memo = {}
        
        def get_dist(c1_idx, c2_idx):
            if c1_idx == -1: return 0  # Initial position is free
            # Keyboard is 6 columns wide
            x1, y1 = divmod(c1_idx, 6)
            x2, y2 = divmod(c2_idx, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        def solve(idx, other_f):
            # Base case: all letters typed
            if idx == len(word):
                return 0
            
            state = (idx, other_f)
            if state in memo:
                return memo[state]
            
            curr_char_idx = ord(word[idx]) - ord('A')
            prev_char_idx = ord(word[idx-1]) - ord('A')
            
            # Option 1: Move the finger that typed the previous character
            # (The finger at word[idx-1] moves to word[idx])
            res1 = get_dist(prev_char_idx, curr_char_idx) + solve(idx + 1, other_f)
            
            # Option 2: Move the "other" finger
            # (The finger at other_f moves to word[idx])
            res2 = get_dist(other_f, curr_char_idx) + solve(idx + 1, prev_char_idx)
            
            memo[state] = min(res1, res2)
            return memo[state]

        # Start from the second character (index 1). 
        # Finger 1 starts at word[0] (cost 0), Finger 2 is "unplaced" (-1)
        return solve(1, -1)