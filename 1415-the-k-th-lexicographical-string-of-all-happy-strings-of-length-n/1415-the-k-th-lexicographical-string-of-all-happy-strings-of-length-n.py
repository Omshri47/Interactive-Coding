class Solution(object):
    def getHappyString(self, n, k):
        result = []
        def solve(current_string):
            if len(result) == k:
                return
            if len(current_string)==n:
                result.append(current_string)
                return
            
            for ch in ['a','b','c']:
                if not current_string or current_string[-1]!=ch:
                    solve(current_string + ch)
                if len(result)==k:
                    break
        solve("")
        if len(result) >= k:
            return result[k-1]
        else:
            return "" 

       
        