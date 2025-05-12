from typing import List
from collections import deque

class Solution:
    def cal(self, one: int, two: int, operand: str) -> int:
        res: int = 0

        if operand == "+":
            res = one + two
        elif operand == "-":
            res = two - one
        elif operand == "*":
            res = one * two
        else:
            res = int(two / one)
        
        return res

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        operand = ["+","-","*","/"]
        s = deque(tokens)
        s2 = deque([])
        res: int = 0
        while len(s) > 0:
            d = s.popleft()
            if d in operand:
                one = s2.pop()
                two = s2.pop()
                nResult = self.cal(int(one), int(two), d)
                res = nResult
                s2.append(nResult)
            else:
                s2.append(d)
        
        return res



# a = ["2", "1", "+","3", "*"]

# b = deque(a)

# for i in range(0, len(a)):
#     print(b.popleft())