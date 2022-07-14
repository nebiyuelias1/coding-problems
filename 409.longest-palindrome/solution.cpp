#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestPalindrome(string s) {
        // "civilwartestingwhether"
        // a: 1
        // b: 1
        // c: 4
        // d: 2
        unordered_map<char, int> umap;

        for (int i = 0; i < s.size(); i++) {
            if (umap.find(s[i]) == umap.end()) {
                umap[s[i]] = 1;
            } else {
                umap[s[i]]++;
            }
        }
        
        int maxLength = 0;
        int maxOdd = 0;
        for (auto& it: umap) {
            if (umap[it.first] % 2 == 0) {
                maxLength += umap[it.first];
            } else {
                maxOdd = max(maxOdd, umap[it.first]);
                maxLength += umap[it.first] - 1;
            }
        }

        if (maxOdd > 0) {
            maxLength -= (maxOdd - 1);
        }
        maxLength += maxOdd;

        return maxLength;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    cout << sol.longestPalindrome("bb") << endl;
    return 0;
}
