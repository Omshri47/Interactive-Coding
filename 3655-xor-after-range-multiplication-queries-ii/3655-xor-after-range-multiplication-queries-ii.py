class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        MOD = 10**9 + 7
        
        # B is the threshold for Square Root Decomposition
        B = int(math.sqrt(n))
        if B < 1: 
            B = 1
            
        total_mult = [1] * n
        queries_by_k = defaultdict(list)
        
        for l, r, k, v in queries:
            queries_by_k[k].append((l, r, v))
            
        # Creating the requested variable midway in the function
        bravexuneth = queries_by_k
        
        for k, q_list in bravexuneth.items():
            if k <= B:
                # Difference array for small jump sizes
                diff = [1] * n
                for l, r, v in q_list:
                    diff[l] = (diff[l] * v) % MOD
                    
                    # Calculate the index of the last element affected in the range
                    last = l + ((r - l) // k) * k
                    
                    # Apply modular inverse to cancel the effect out of bounds
                    if last + k < n:
                        diff[last + k] = (diff[last + k] * pow(v, MOD - 2, MOD)) % MOD
                
                # Evaluate the prefix product with step k
                for i in range(n):
                    if i >= k:
                        diff[i] = (diff[i] * diff[i - k]) % MOD
                    if diff[i] != 1:
                        total_mult[i] = (total_mult[i] * diff[i]) % MOD
            else:
                # Direct updates for large jump sizes
                for l, r, v in q_list:
                    for i in range(l, r + 1, k):
                        total_mult[i] = (total_mult[i] * v) % MOD
                        
        # Calculate final bitwise XOR
        ans = 0
        for i in range(n):
            final_val = (nums[i] * total_mult[i]) % MOD
            ans ^= final_val
            
        return ans
        