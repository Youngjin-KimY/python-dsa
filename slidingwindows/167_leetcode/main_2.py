from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        eidx: int = len(numbers) - 1
        res: List[int] = []
        for i in range(0, len(numbers)):
            sv: int = numbers[i]
            ev: int = numbers[eidx]
            sub_sum = sv+ev
            while (i < eidx) and (sub_sum >= target):
            
                
                # 1 2 4 5 6
                # 1,2,3,4,4,19,10,90
                if sub_sum == target:
                    res = [i+1, eidx + 1]
                    break

                eidx = eidx - 1
                sub_sum = numbers[i] + numbers[eidx]
            
            if len(res) != 0:
                break
        
        return res
            
