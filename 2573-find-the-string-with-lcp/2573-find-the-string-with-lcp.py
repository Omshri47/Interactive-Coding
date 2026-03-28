class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        
        """
        n = len(lcp)
        word = [""] * n
        current_char = 'a'
        
        for i in range(n):
            if not word[i]:
                if current_char > 'z':
                    return ""
                
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = current_char
                
                current_char = chr(ord(current_char) + 1)
                
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    expected = 1 + (lcp[i+1][j+1] if i + 1 < n and j + 1 < n else 0)
                else:
                    expected = 0
                
                if lcp[i][j] != expected:
                    return ""
                    
        return "".join(word)
        