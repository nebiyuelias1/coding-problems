#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        vector<int> ans;

        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                ans.push_back(left + 1);
                ans.push_back(right + 1);
                return ans;
            } else if (sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            }
        }

        return ans;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> k {2,7,11,15};
    sol.twoSum(k, 9);
    return 0;
}
