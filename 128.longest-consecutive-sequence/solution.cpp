#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> hashMap;
        for (auto& n: nums) {
            hashMap[n] = 1;
        }

        int longestConsecutive = 0;
        for (auto& num: nums) {
            if (hashMap.find(num-1) == hashMap.end()) {
                int currentConsecutive = 1;
                int current = num;
                while (hashMap.find(current + 1) != hashMap.end()) {
                    current += 1;
                    currentConsecutive++;
                }
                longestConsecutive = max(currentConsecutive, longestConsecutive);
            }
        }

        return longestConsecutive;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol;
    vector<int> v {0,3,7,2,5,8,4,6,0,1};
    cout << sol.longestConsecutive(v) << endl;
    return 0;
}