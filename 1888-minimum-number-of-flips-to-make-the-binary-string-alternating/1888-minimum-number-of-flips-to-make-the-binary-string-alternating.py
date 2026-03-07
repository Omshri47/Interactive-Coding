class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        doubled_s = s + s
        diff1, diff2=0, 0
        ans = float('inf')

        left = 0
        for right in range(len(doubled_s)):
            if doubled_s[right]!=('0' if right %2==0 else '1'):
                diff1 +=1
            if doubled_s[right]!=('1'if right % 2 ==0 else '0'):
                diff2+=1

            if(right - left+1)>n:
                if doubled_s[left]!=('0'if left % 2 == 0  else '1'):
                    diff1-=1
                if doubled_s[left]!=('1'if left % 2 == 0  else '0'):
                    diff2-=1
                left +=1

            if (right - left + 1) == n:
                ans = min(ans,diff1,diff2)

        return ans