#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int n = nums.size();

        for (int i = 1; i <= n; i++) {
            if (nums[i-1] == nums[i]) {
                return nums[i];
            }
        }

        return -1;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> nums {1,1};
    cout << s.findDuplicate(nums);
    return 0;
}