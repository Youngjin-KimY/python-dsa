from typing import List

class Solution:

    def binarySearch(self, tar: int, nums: List[int])-> int:
        si: int = 0
        ei: int = len(nums) - 1
        
        while si <= ei:
            mid = si + int((ei-si)/2)

            if nums[mid] ==  tar:
                return mid
    
            elif nums[mid] > tar:
                ei = mid - 1
            else:
                si = mid + 1


        return -1001


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res: List[int] = []

        for i in range(0, len(numbers)):
            f: int = numbers[i]
            e: int = target - f
            eidx: int = self.binarySearch(e, numbers)
            if eidx != -1001:
                if eidx != i:
                    res = [i+1, eidx+1]
                else:
                    if numbers[i-1] == numbers[i]:
                        res = [i+1, i]
                    else:
                        res = [i+1, i+2]
                break


        return res
    

if __name__ == "__main__":
    s = Solution()
    # nums = [1,2,3,4,5]
    # ans = s.binarySearch(5, nums)
    # print(ans)

    nums = [2,7,11,19]
    target = 9
    ans = s.twoSum(nums, target)
    print(ans)