class Solution {
public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
       
        int MOD = 1000000007;
        
        // Process each query
        for (const auto& q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            for (int idx = l; idx <= r; idx += k) {
                // 1LL casts nums[idx] to a 64-bit long long to prevent overflow during multiplication
                nums[idx] = (1LL * nums[idx] * v) % MOD;
            }
        }
        
        // Calculate the bitwise XOR of the modified array
        int ans = 0;
        for (int num : nums) {
            ans ^= num;
        }
        
        return ans;
    }
};