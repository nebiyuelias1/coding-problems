# https://leetcode.com/problems/gas-station/submissions/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_sum = sum(gas)
        cost_sum = sum(cost)

        diff = gas_sum - cost_sum
        if diff < 0:
            return -1

        tank = 0
        start_index = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start_index = i + 1

        return start_index


sol = Solution()
print(sol.canCompleteCircuit([2,3,4], [3,4,3]))
