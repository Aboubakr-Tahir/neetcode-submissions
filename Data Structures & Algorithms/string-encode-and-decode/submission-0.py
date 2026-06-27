class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs :
            length = str(len(s))
            res += length+'@'+s
        print(">>>", repr(res), "<<<")
        return res
    def decode(self, s: str) -> List[str]:
        i=0
        res = []
        string = ''
        while i < len(s) :
            j=i
            while s[j] != '@' :
                j+=1
                print(j)
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length
        return res
