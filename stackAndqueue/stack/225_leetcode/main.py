from typing import List

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque([])
        

    def push(self, x: int) -> None:
        self.q.append(x)
        if len(self.q) >= 2:
            for _ in range(0, len(self.q) - 1):
                d = self.q.popleft()
                self.q.append(d)

    def pop(self) -> int:
        res: int = self.q.popleft()
        return res

    def top(self) -> int:
        if len(self.q) == 0:
            return None
        if len(self.q) == 1:
            res = self.q.popleft()
            self.q.append(res)
            return res
        
        res: int = self.q.popleft()
        self.q.append(res)
        for i in range(0, len(self.q) - 1):
            d = self.q.popleft()
            self.q.append(d)
        return res


    def empty(self) -> bool:
        res: bool = True
        if len(self.q) == 0: 
            res = True 
        else: 
            res = False
        return res
    

s = MyStack()

s.push(1)
s.push(2)
print(s.q)
print(s.empty())
print(s.top())
print(s.pop())
print(s.top())
print(s.pop())
print(s.empty())