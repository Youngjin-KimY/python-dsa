from typing import List, Tuple

class binary_search:
    def __init__(self):
        pass

    def search(self, lst: List[int], target: int) -> Tuple[int, int]:
        
        left_idx: int = 0
        right_idx: int = len(lst) - 1
        point: int = int((left_idx + right_idx) / 2)
        while left_idx < right_idx:
            if lst[point] > target:
                right_idx = point - 1
                point = int((left_idx + right_idx) / 2)
            elif lst[point] < target:
                left_idx = point + 1
                point = int((left_idx + right_idx) / 2)
        
        if target != lst[point]:
            return (-1,-1)

        return (point, lst[point])

if __name__ == "__main__":
    s = binary_search()
    ans = s.search([1,2,3,4,6,7,8,9,10],10)
    print(ans)