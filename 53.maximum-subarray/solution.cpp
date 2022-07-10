#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int max(int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }

    int maxSubArray(vector<int> &nums)
    {
        int size = nums.size();
        int max = -100000;
        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += nums[i];
            sum = this->max(nums[i], sum);
            max = this->max(max, sum);
        }
        return max;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v {-2,1,-3,4,-1,2,1,-5,4};
    cout << sol.maxSubArray(v) << endl;
    return 0;
}
