#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        unordered_map<int,int> visited;
        for (int i = 0; i < nums.size(); i++) {
            if (visited.find(target - nums[i]) != visited.end()) {
                ans.push_back(visited[target-nums[i]]);
                ans.push_back(i);
                return ans;
            } else {
                visited[nums[i]] = i;
            }
        }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v {-1,-2,-3,-4,-5};
    sol.twoSum(v, -8);
    return 0;
}
