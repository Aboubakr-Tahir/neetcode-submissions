class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hash_map = {
            '+' : lambda a,b : a + b,
            '*' : lambda a,b : a * b,
            '-' : lambda a,b : a - b,
            '/' : lambda a,b : int(a / b)
        }
        curr_arr = []
        for token in tokens :
            if token not in hash_map :
                curr_arr.append(int(token))
            else :
                result = hash_map[token](curr_arr[-2],curr_arr[-1])
                curr_arr.pop()
                curr_arr.pop()
                curr_arr.append(result)
        return curr_arr[-1]
