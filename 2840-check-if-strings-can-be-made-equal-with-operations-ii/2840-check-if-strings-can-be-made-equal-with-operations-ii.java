class Solution {
    public boolean checkStrings(String s1, String s2) {
        int[] evenCounts = new int[26];
        int[] oddCounts = new int[26];
        
        for (int i = 0; i < s1.length(); i++) {
            int charS1 = s1.charAt(i) - 'a';
            int charS2 = s2.charAt(i) - 'a';
            
            if (i % 2 == 0) {
                evenCounts[charS1]++;
                evenCounts[charS2]--;
            } else {
                oddCounts[charS1]++;
                oddCounts[charS2]--;
            }
        }
        
        for (int i = 0; i < 26; i++) {
            if (evenCounts[i] != 0 || oddCounts[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
}