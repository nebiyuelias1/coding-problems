#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int sum = 0, count = 0;
        unordered_map<int, int> sumCount;
        sumCount[0] = 1;

        for (int i = 0; i < n; i++)
        {
            sum += nums[i];
            int diff = sum - k;
            if (sumCount.find(diff) != sumCount.end()) {
                count += sumCount[diff];
            }

            if (sumCount.find(sum) != sumCount.end()) {
                sumCount[sum] += 1;
            } else {
                sumCount[sum] = 1;
            }
        }
        return count;
    }
};

int main(int argc, char const *argv[])
{
    
    return 0;
}