class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs :
            res += str(len(s)) + '@' + s
        print(res)
        return res 
    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        while i < len(s) :
            j=i
            while j<len(s) and s[j] != '@' :
                j+=1
            print(s[i:j])
            length= int(s[i:j])
            i = j+1
            res.append(s[i:i+length])
            i = i+length
        return res