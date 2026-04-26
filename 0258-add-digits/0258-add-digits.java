class Solution {
    public int addDigits(int num) {
        while (num > 9) {
            int currentSum = 0;
            while (num > 0) {
                currentSum += num % 10;
                num /= 10;
            }
            num = currentSum;
        }
        return num;
    }
}