
class Solution {
private:
    // Define the mapping as a member of the class
    const vector<string> mapping = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    // Helper function for backtracking
    void backtrack(string& digits, int index, string& current, vector<string>& result) {
        // Base case: if the current string length matches input digits length
        if (index == digits.length()) {
            result.push_back(current);
            return;
        }

        // Convert char digit to integer index
        string letters = mapping[digits[index] - '0'];
        
        for (char c : letters) {
            current.push_back(c);           // Choose
            backtrack(digits, index + 1, current, result); // Explore
            current.pop_back();              // Backtrack (remove last char)
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        
        vector<string> result;
        string current = "";
        backtrack(digits, 0, current, result);
        return result;
    }
};