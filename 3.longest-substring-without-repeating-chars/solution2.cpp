#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int size = s.size();
        int maxLength = 0;
        unordered_map<char, int> frequency;

        int left = 0;
        int right = 0;

        while (right < size) {
            if (frequency.find(s[right]) == frequency.end()) {
                frequency[s[right]] = 1;
                right++;
                maxLength = max(maxLength, right-left);
            } else {
                frequency.erase(s[left]);
                left++;
            }

        }

        return maxLength;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    cout << sol.lengthOfLongestSubstring("dvdf") << endl;
    return 0;
}

