class Solution {
public:
    int romanToInt(std::string s) {
        // Map characters to their corresponding integer values
        std::unordered_map<char, int> romanMap = {
            {'I', 1},   {'V', 5},   {'X', 10},  {'L', 50},
            {'C', 100}, {'D', 500}, {'M', 1000}
        };

        int total = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            // If the current value is less than the next value, subtract it
            if (i + 1 < n && romanMap[s[i]] < romanMap[s[i + 1]]) {
                total -= romanMap[s[i]];
            } else {
                // Otherwise, add it
                total += romanMap[s[i]];
            }
        }

        return total;
    }
};




