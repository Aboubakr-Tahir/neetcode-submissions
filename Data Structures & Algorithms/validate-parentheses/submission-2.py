class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = { "}" : "{","]":"[",")":"("}

        for char in s :
            if char in hash_map :
                if stack and hash_map[char] == stack[-1] :
                    stack.pop()
                else :
                    return False
            else : 
                stack.append(char)
        return True if not stack else False