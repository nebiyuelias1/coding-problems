#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        
        if (n == 1 || n == 0) {
            return n;
        }

        int ans = -1;

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i-1]) {
                ans = i + 1;
                continue;
            }

            int j = i + 1;
            while ((j < n) && nums[i-1] >= nums[j]) j++;

            if (j == n) {
                ans = i;
                break;
            }
            nums[i] = nums[j];
        }

        return ans;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v {1, 2};
    sol.removeDuplicates(v);
    return 0;
}
