class Solution {
    public int xorAfterQueries(int[] nums, int[][] queries) {
        int MOD = 1000000007;
        
        // Process each query
        for (int[] q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            for (int idx = l; idx <= r; idx += k) {
                // Cast to long (1L) to prevent overflow during multiplication
                nums[idx] = (int) ((1L * nums[idx] * v) % MOD);
            }
        }
        
        // Calculate the bitwise XOR of the modified array
        int ans = 0;
        for (int num : nums) {
            ans ^= num;
        }
        
        return ans;
    }
}