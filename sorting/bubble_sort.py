from typing import List

class Solution:
    def __init__(self):
        pass

    def swap(self, lst: List[int], a: int, b :int) -> None:
        tmp = lst[a]
        lst[a] = lst[b]
        lst[b] = tmp

    def bubble_sort(self, lst: List[int]) -> None:
        swaped : bool = True

        while swaped:

            swaped = False
            for i in range(1, len(lst)):
                if lst[i] < lst[i-1]:
                    self.swap(lst, i-1, i)
                    swaped = True
        
        for i in range(0, len(lst)):
            print(lst[i], end=" ")
                
    

if __name__ == "__main__":
    t_lst = [27,1,3,7,2,5]
    s = Solution()
    s.bubble_sort(t_lst)






        
