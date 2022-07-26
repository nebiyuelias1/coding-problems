#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxIndex = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++)
        {
            if (maxIndex >= (n-1)) {
                return true;
            }
            if (maxIndex < i) {
                return false;
            }

            maxIndex = max(maxIndex, i + nums[i]);
        }

        return false;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> v {2, 2, 1, 0, 1, 0, 4};
    s.canJump(v);
    return 0;
}
