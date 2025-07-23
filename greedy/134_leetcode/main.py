from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        n = len(gas)
        fuelRemain = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            fuelRemain += diff

            if fuelRemain < 0:
                start = i + 1
                fuelRemain = 0
        
        return start