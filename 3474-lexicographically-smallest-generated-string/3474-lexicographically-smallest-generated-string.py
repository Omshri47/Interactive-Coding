class Solution(object):
    def generateString(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n = len(str1)
        m = len(str2)
        N = n + m - 1
        
        ans = ['?'] * N
        
        # Phase 1: Enforce all 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if ans[i + j] != '?' and ans[i + j] != str2[j]:
                        return ""  # Contradiction in forced characters
                    ans[i + j] = str2[j]
                    
        # Phase 2: Track 'F' constraints and their last '?'
        constraints_ending_at = [[] for _ in range(N)]
        
        for i in range(n):
            if str1[i] == 'F':
                last_q_idx = -1
                for j in range(i, i + m):
                    if ans[j] == '?':
                        last_q_idx = max(last_q_idx, j)
                        
                if last_q_idx == -1:
                    # Constraint has no '?', check immediately if it violates the 'F' rule
                    match = True
                    for j in range(m):
                        if ans[i + j] != str2[j]:
                            match = False
                            break
                    if match:
                        return ""
                else:
                    # Register this 'F' constraint to be resolved at its last '?'
                    constraints_ending_at[last_q_idx].append(i)
                    
        # Phase 3: Greedily assign '?' from left to right
        for k in range(N):
            if ans[k] == '?':
                forbidden = set()
                
                # Check constraints that rely on this exact '?' to not fail
                for i in constraints_ending_at[k]:
                    match = True
                    for j in range(m):
                        if i + j == k:
                            continue  # Skip the '?' we are currently evaluating
                        if ans[i + j] != str2[j]:
                            match = False
                            break
                            
                    # If everything else matches, we are forbidden from completing the match
                    if match:
                        forbidden.add(str2[k - i])
                        
                # Greedily pick the smallest valid character
                placed = False
                for c_code in range(97, 123):  # ASCII 'a' to 'z'
                    c = chr(c_code)
                    if c not in forbidden:
                        ans[k] = c
                        placed = True
                        break
                        
                if not placed:
                    return ""
                    
        return "".join(ans)
        