class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s :
            if c in closed_brackets and stack: 
                if stack[-1] == closed_brackets[c]:
                    stack.pop(-1)
                else : 
                    return False
            else :
                stack.append(c)
        if stack : 
            return False
        else : 
            return True