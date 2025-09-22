from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        sub = []

        keybord = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

        def stringsum(liststr: List[str]):
            res = ""
            
            if len(liststr) == 0:
                return None
            
            for c in liststr:
                res+=c
            
            return res

        def runDfs(charac: str):
            if charac == "":
                completedString = stringsum(sub)
                if completedString != None:
                    res.append(completedString)
                return

            currentDigit = int(charac[0])
            curChar = keybord[currentDigit]

            for i in curChar:
                sub.append(i)
                runDfs(charac[1:])
                sub.pop()

        runDfs(digits)

        return res