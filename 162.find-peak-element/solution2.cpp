#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (left  < right) {
            int mid = (left + right) / 2;
            if (nums[mid] > nums[mid+1]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v{1, 2, 3, 1};
    cout << sol.findPeakElement(v);
    return 0;
}