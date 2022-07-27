#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<string> distinctSubsequencesRec(string s, int index, int n, string original)
    {
        if (index >= n) {
            return vector<string> {s};
        }

        string t = s;
        int i = t.find(original[index]);
        t.erase(i, 1);
        vector<string> a  = this->distinctSubsequencesRec(s, index + 1, n, original);
        vector<string> b = this->distinctSubsequencesRec(t, index + 1, n, original);
        vector<string> combined;
        combined.reserve(a.size() + b.size());
        combined.insert(combined.end(), a.begin(), a.end());
        combined.insert(combined.end(), b.begin(), b.end());
        return combined;
    }

    vector<string> distinctSubsequences(string s)
    {
        int n = s.size();
        return this->distinctSubsequencesRec(s, 0, n, s);
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<string> ans = s.distinctSubsequences("abcd");
    for (int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << endl;
    }
    
}