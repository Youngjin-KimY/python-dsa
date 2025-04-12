from typing import List

class counting_sort:
    def __init__(self):
        pass

    def counting_sort(self, lst: List[int]) -> List[int]:
        max: int = 0

        for i in range(0, len(lst)):
            if max < lst[i]:
                max = lst[i]
    
        counting_arr: List[int] = [0 for _ in range(0, max + 1)]

        for i in range(0, len(lst)):
            counting_arr[lst[i]] += 1
    
        # cumlative
        for i in range(1, len(counting_arr)):
            counting_arr[i] += counting_arr[i-1]

        output_arr: List[int] = [0 for _ in range(0, len(lst))]
        
        for i in range(len(lst)-1, -1, -1):
            output_arr[counting_arr[lst[i]] - 1] = lst[i]
            counting_arr[lst[i]] -= 1


        return output_arr

if __name__ == "__main__":
    a = [_ for _ in range(0, 5)]
    print(a)
    for i in range(1, len(a)):
        a[i] += a[i-1]
    print(a)