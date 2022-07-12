#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int findPeakElement(vector<int> &nums)
    {
        int size = nums.size();

        if (size == 1)
        {
            return 0;
        }

        int peakIndex = 0;

        for (int i = 0; i < size; i++)
        {
            if (i == 0)
            {
                if (nums[i] > nums[i + 1])
                {
                    peakIndex = i;
                }
            }
            else if ((i + 1) == size)
            {
                if (nums[i] > nums[i - 1])
                {
                    peakIndex = i;
                }
            }
            else if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1])
            {
                peakIndex = i;
            }
        }

        return peakIndex;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v{1, 2, 3, 1};
    cout << sol.findPeakElement(v);
    return 0;
}