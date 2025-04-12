from typing import List
from counting_sort import counting_sort

class radix_sort:
    def __init__(self):
        self.count_sort = counting_sort()

    def radix_sort(self, lst:List[int]) -> List[int]:
        max1 = max(lst)

        exp = 1

        # while max1 / exp >= 1:
        #     self.count_sort.counting_sort(lst)

        return []
    
if __name__ == "__main__":
    a = [0] * (10)
    print(a)