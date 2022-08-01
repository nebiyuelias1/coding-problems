#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    
    int numDecodings(string s)
    {
        int n = s.size();
        int prev = 1;
        int prevPrev = 0;
        
        for (int i = 0; i < n; i++)
        {
            int ways = 0;
            if (s.substr(i, 1) != "0") {
                ways += prev;
            }

            if ((i-1) >= 0 && s.substr(i-1, 2) >= "10" && s.substr(i-1, 2) <= "26") {
                ways += prevPrev;
            }

            prevPrev = prev;
            prev = ways;
        }
        
        return prev;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    s.numDecodings("06");
    return 0;
}