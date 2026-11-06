class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            length = len(word)
            s += f'{length}@{word}'
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        if s == "0@" :
            return [""]
        res = []
        i = 0
        while i < len(s) : 
            length = ""
            while s[i] != '@':
                length += s[i]
                i += 1
            j = int(length)
            i += 1    
            res.append(s[i:i+j])
            i = i+j
        print(res)
        return res