from typing import List

class merge_sort:
    def __init__(self):
        pass

    def merge(self, pre_list: List[int], back_list: List[int]) -> List[int]:

        res: List[int] = []
        pre_pointer: int = 0      
        back_pointer: int = 0

        while len(pre_list) > pre_pointer and len(back_list) > back_pointer:
            v_pre = pre_list[pre_pointer]
            v_back = back_list[back_pointer]

            if v_pre > v_back:
                res.append(v_back)
                back_pointer+=1
            elif v_pre < v_back:
                res.append(v_pre)
                pre_pointer+=1
            else:
                res.append(v_pre)
                res.append(v_back)
                pre_pointer+=1
                back_list+=1  

        while len(pre_list) > pre_pointer:
            res.append(pre_list[pre_pointer])
            pre_pointer+=1

        while len(back_list) > back_pointer:
            res.append(back_list[back_pointer])
            back_pointer+=1

        return res

    def merge_sort(self, lst: List[int]) -> List[int]:
        if len(lst) == 1:
            return lst

        mid: int = int(len(lst)/2)
        pre_list: List[int] = lst[0:mid]
        back_list: List[int] = lst[mid:]

        sorted_pre_list: List[int] = self.merge_sort(pre_list)
        sorted_back_list: List[int] = self.merge_sort(back_list)

        res: List[int] = self.merge(sorted_pre_list, sorted_back_list)

        return res

    


if __name__ == "__main__":
    m = merge_sort()
    a = [1,2,3,4,5]
    b=  [5,3,2,1,4]
    c = [100, 23, 12,3,5,8]

    aa = m.merge_sort(a)
    print(aa)
    bb = m.merge_sort(b)
    print(bb)
    cc = m.merge_sort(c)
    print(cc)