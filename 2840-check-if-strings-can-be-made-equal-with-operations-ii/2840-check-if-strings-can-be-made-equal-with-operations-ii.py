class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Arrays to store frequencies of each lowercase letter (26 letters)
        even_counts = [0] * 26
        odd_counts = [0] * 26
        
        for i in range(len(s1)):
            # Get the alphabetical index (0-25) for the characters
            char_s1 = ord(s1[i]) - ord('a')
            char_s2 = ord(s2[i]) - ord('a')
            
            if i % 2 == 0:
                even_counts[char_s1] += 1
                even_counts[char_s2] -= 1
            else:
                odd_counts[char_s1] += 1
                odd_counts[char_s2] -= 1
                
        # If any count is not zero, the character pools don't match
        for i in range(26):
            if even_counts[i] != 0 or odd_counts[i] != 0:
                return False
                
        return True
        