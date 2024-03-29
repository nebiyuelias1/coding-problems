#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.length();
        int m = text2.length();
        
        vector<vector<int>> dp;
        for (int i = 0; i < n + 1; i++)
        {
            vector<int> row {0};
            dp.push_back(row);
        }

        for (int i = 1; i < m + 1; i++) {
            dp[0].push_back(0);
        }

        for (int i = 1; i < n + 1; i++)
        {
            for (int j = 1; j < m + 1; j++)
            {
                if (text1[i-1] == text2[j-1]) {
                    dp[i].push_back(1 + dp[i-1][j-1]);
                } else {
                    dp[i].push_back(max(dp[i-1][j], dp[i][j-1]));
                }
            }
        }

        return dp[n][m];
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    sol.longestCommonSubsequence("abc", "def");
    return 0;
}