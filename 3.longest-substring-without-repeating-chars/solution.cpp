#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int size = s.size();
        int maxLength = 0;
        unordered_map<char, int> frequency;
        int count = 0;

        for (int i = 0; i < size; i++) {
            int localIndex = i;
            while (localIndex < size && frequency.find(s[localIndex]) == frequency.end()) {
                frequency[s[localIndex]] = 1;
                count++;
                localIndex++;
            }
            maxLength = count > maxLength ? count : maxLength;
            frequency.clear();
            count = 0;
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

