#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int numDecodingsRec(string s, int i, int n, unordered_map<int, int>& memo)
    {
        if (i == n)
        {
            return 1;
        }

        if (i > n)
        {
            return 0;
        }

        if (memo.find(i) != memo.end()) {
            return memo[i];
        }

        int sum = 0;

        int lengthOneSubStr = stoi(s.substr(i, 1));
        if (lengthOneSubStr >= 1)
        {
            sum += this->numDecodingsRec(s, i + 1, n, memo);

            int lengthTwoSubStr = stoi(s.substr(i, 2));
            if (lengthTwoSubStr >= 1 && lengthTwoSubStr <= 26)
            {
                sum += this->numDecodingsRec(s, i + 2, n, memo);
            }
        }

        memo[i] = sum;

        return sum;
    }

    int numDecodings(string s)
    {
        int n = s.size();
        unordered_map<int, int> memo;
        return numDecodingsRec(s, 0, n, memo);
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    s.numDecodings("06");
    return 0;
}