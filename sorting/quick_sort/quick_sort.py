from typing import List

class quick_sort:
    def __init__(self):
        pass

    def partition(self, lst: List[int], start: int, end: int) -> int:
        ## TO-DO 
        # partitioning
        start_idx = start
        end_idx = end - 1
        pivot = lst[end]
    
        while start_idx <= end_idx:
            
            # right
            while end_idx >= start_idx:
                if  pivot > lst[end_idx]:
                    break
                end_idx -= 1
                

            # left
            while start_idx <= end_idx:
                if pivot < lst[start_idx]:
                    break
                start_idx += 1

            if start_idx <= end_idx:
                lst[end_idx], lst[start_idx] = lst[start_idx], lst[end_idx] 

        pivot_idx: int = end_idx + 1

        lst[pivot_idx], lst[end] = lst[end], lst[pivot_idx]

        return pivot_idx

    def quick_sort(self, lst: List[int], start: int, end: int):
        if start >= end:
            return
        
        pivot_idx: int = self.partition(lst, start, end)
        self.quick_sort(lst, start, pivot_idx-1)
        self.quick_sort(lst, pivot_idx+1, end)

        # print(lst)
        

if __name__ == "__main__":
    q = quick_sort()
    lst = [2,5,3,22,1,11,4,8,9,10,7,31]
    # 2 5 3 4 |7| 8 9 10 11
    # 2 3 |4| 5   8 9 
    q.quick_sort(lst, 0, len(lst)-1)
    print(lst)



