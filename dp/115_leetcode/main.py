class Solution:
    
        
    def numDistinct(self, s: str, t: str) -> int:
        res_cnt = 0
        def comm(i:int, path:str, t: str):
            nonlocal res_cnt
            if path == t:
                res_cnt = res_cnt + 1
                return 

            for x in range(i, len(s)):
                cur_leng = len(path)
                if t[cur_leng] != s[x]:
                    continue
                path += s[x]
                comm(x+1, path, t)
                path = path[:-1]


        
        comm(0,"",t)

        return res_cnt
#     r a b b b i t
# 0 0 0 0 0 0 0 0 0
# r 0 1 0 0 0 0 0 0
# a 0 0 1 1 1 1 1 1
# b 0 0 0 1 2 3 3 3
# b 0 0 0 0 1 3 3 3
# i 0 0 0 0 0 0 3 3
# t 0 0 0 0 0 0 0 3
#

#    " " r a b b b i t
# " " 1  1 1 1 1 1 1 1 i0 
#  r  0  1 1 1 1 1 1 1 i1
#  a  0  0 1 1 1 1 1 1 i2
#  b  0  0 0 1 2 3 3 3 i3
#  b  0  0 0 0 1 3 3 3 i4
#  i  0  0 0 0 0 0 3 3 i5
#  t  0  0 0 0 0 0 0 3 i6