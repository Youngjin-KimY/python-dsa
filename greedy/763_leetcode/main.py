from typing import List

class Solution:

    def transformation(self, s: str) -> List[List[int]]:
        filter = set([])
        for i in range(0, len(s)):
            filter.add(s[i])
        
        charLen = 0
        for ch in filter:
            if ord(ch) - 96 > charLen:
                charLen = ord(ch) - 96
            
        table = [[-1,-1] for _ in range(0, charLen)]

        for i in range(0, len(s)):
            t = table[ord(s[i])-97]
            if t[0] == -1:
                t[0] = i
                t[1] = i
            else:
                t[1] = i

            table[ord(s[i])-97] = t
        
        table.sort()
        startIdx = -1
        for i in range(0, len(table)):
            if table[i][0] == -1:
                startIdx = i

        return table[startIdx+1:]

    def partitionLabels(self, s: str) -> List[int]:
        table = self.transformation(s)
        # table.sort(key=lambda x:x[1])
        res = []
        start, prevEnd = table[0]

        for entry in table[1:]:
            # if start == -1:
            #     start, prevEnd = entry
            #     continue
            nstart, nend = entry
            if prevEnd > nstart:
                start = min(start, nstart)
                prevEnd = max(prevEnd, nend)
            else:
                res.append(prevEnd-start+1)
                start, prevEnd = entry

        res.append(prevEnd - start + 1)
        # if table[-1][0] == table[-1][1] and table[-1][0] == (len(table)-1):
        #     res.append(1)

        return res