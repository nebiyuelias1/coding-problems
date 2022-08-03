#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int longestCommonSubsequenceRec(string text1, string text2, int i, int j, unordered_map<string, int> &memo)
    {
        string key = to_string(i) + "," + to_string(j);

        if (memo.find(key) != memo.end())
        {
            return memo[key];
        }

        if (i == text1.size() || j == text2.size())
        {
            return 0;
        }

        int ans; 

        if (text1[i] == text2[j])
        {
            ans = 1 + this->longestCommonSubsequenceRec(text1, text2, i + 1, j + 1, memo);
            memo[key] = ans;
            return ans;
        }

        ans = max(this->longestCommonSubsequenceRec(text1, text2, i + 1, j, memo),
                      this->longestCommonSubsequenceRec(text1, text2, i, j + 1, memo));
        memo[key] = ans;
        return ans;
    }

    int longestCommonSubsequence(string text1, string text2)
    {
        unordered_map<string, int> memo;
        return this->longestCommonSubsequenceRec(text1, text2, 0, 0, memo);
    }
};

int main(int argc, char const *argv[])
{

    return 0;
}