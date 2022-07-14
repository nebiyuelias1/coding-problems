#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int rec(string haystack, string needle, int left, int right, unordered_map<string, int>& memo) {
        string sub = haystack.substr(left, right-left+1);
        if (sub == needle) {
            return left;
        }

        if (left >= right) {
            return -1;
        }

        if (memo.find(sub) != memo.end()) {
            return memo[sub];
        }

        int option1 = this->rec(haystack, needle, left, right-1, memo);
        int option2 = this->rec(haystack, needle, left+1, right, memo);

        int ans = option1 != -1 ? option1 : option2;
        memo[sub] = ans;
        return memo[sub];
    }

    int strStr(string haystack, string needle) {
        if (needle.size() == 0) {
            return 0;
        }
        
        if (haystack == needle) {
            return 0;
        }

        int left = 0;
        int right = haystack.size() - 1;

        unordered_map<string, int> memo;

        int option1 = this->rec(haystack, needle, left, right-1, memo);
        int option2 = this->rec(haystack, needle, left+1, right, memo);

        return option1 != -1 ? option1 : option2;    
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.strStr("abbbbbaabbaabaabbbaaaaabbabbbabbbbbaababaabbaabbbbbababaababbbbaaabbbbabaabaaaabbbbabbbaabbbaabbaaabaabaaaaaaaa", "abbbaababbbabbbabbbbbabaaaaaaabaabaabbbbaabab") << endl;
    return 0;
}
