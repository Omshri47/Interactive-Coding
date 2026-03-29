class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
  

        even_match = (s1[0] == s2[0] and s1[2] == s2[2]) or \
                     (s1[0] == s2[2] and s1[2] == s2[0])
        
 
        odd_match = (s1[1] == s2[1] and s1[3] == s2[3]) or \
                    (s1[1] == s2[3] and s1[3] == s2[1])
        
  
        return even_match and odd_match