from typing import List

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        candidates = ["(",")"]
        stringLength = 2*n
        res = []
        def backtracking(ing: str, openNumber: int, closeNumber: int):
            if len(ing) == stringLength:
                res.append(ing[:])
                return

            for candidate in candidates:
                if candidate == "(":
                    if openNumber < n:
                        ing += candidate
                        openNumber += 1
                    else:
                        continue
                else:
                    if openNumber > closeNumber:
                        ing += candidate
                        closeNumber += 1
                    else:
                        continue
                backtracking(ing, openNumber, closeNumber)
                deleteStr = ing[len(ing)-1]
                ing = ing[:len(ing)-1]     
                if deleteStr == "(":
                    openNumber -= 1
                else:
                    closeNumber -= 1 
        backtracking("", 0, 0)        
        
        return res


# a = "abcde"
# b = a[:len(a)-1]
# print(a)
# print(b)
# c = a[:]
# print(c)
            


    # def isValidParenthsis(self, parenthsis: str) -> bool:
        
    #     s1 = []
    #     s2 = []

    #     for charP in parenthsis:
    #         s1.append(charP)
        
    #     while s1:
    #         tmp = s1.pop()
    #         if tmp == ")":
    #             s2.append(tmp)
    #         else:
    #             if len(s2) == 0:
    #                 return False

    #             tmpsS2 = s2.pop()
    #             if tmpsS2 == "(":
    #                 s2.append(tmpsS2)
        
    #     if len(s2) > 0:
    #         return False

    #     return True


    # def generateParenthesis(self, n: int) -> List[str]:
    #     a = ["(",")"]
    #     b = ["("]
    #     c = [")"]
    #     levelParentsisRange =[1,2,1]
    #     ing = []
    #     res = []
    #     stringLength = 2*n
    #     def runDfs(idx: int):
    #         if len(ing) == stringLength:
    #             subsum = ""
    #             for i in range(stringLength):
    #                 subsum += ing[i]
    #             if self.isValidParenthsis(subsum):
    #                 res.append(subsum)
    #             return
            
    #         levelRange = 0
    #         if idx == 0 or idx == stringLength-1:
    #             levelRange = levelParentsisRange[0]
    #         else:
    #             levelRange = levelParentsisRange[1]
            

    #         for i in range(levelRange):
    #             if idx == 0:
    #                 ing.append(b[i])
    #             elif idx == stringLength-1:
    #                 ing.append(c[i])
    #             else:
    #                 ing.append(a[i])
                
    #             runDfs(idx + 1)
    #             ing.pop()
        
    #     runDfs(0)




    #     return res
    

# a = "hello"
# b = a
# b+="1"
# print(a)
# print(b)
# a = "hello"
# for ch in a:
#     print(ch)