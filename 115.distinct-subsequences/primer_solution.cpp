#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    void distinctSubsequencesRec(string subsequence, vector<string>& subsequences, int index, string original)
    {
        if (index == (original.size())) {
            subsequences.push_back(subsequence);
        } else {
            this->distinctSubsequencesRec(subsequence, subsequences, index + 1, original);
            this->distinctSubsequencesRec(subsequence + original.at(index), subsequences, index + 1, original);
        }

    }

    vector<string> distinctSubsequences(string s)
    {
        vector<string> v;
        this->distinctSubsequencesRec("", v, 0, s);
        return v;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<string> ans = s.distinctSubsequences("babgbag");
    for (int i = 0; i < ans.size(); i++)
    {
        cout << i << ":" << ans[i] << "," << ans[i].compare("bag") << endl;
    }
    
}