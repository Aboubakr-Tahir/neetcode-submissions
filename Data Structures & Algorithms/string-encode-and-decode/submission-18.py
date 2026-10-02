class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs :
            s += string + "@aba&jcjecbzeiobcez&@"
        return s
    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        i = 0
        while i < len(s) :
            if s[i]!="@" : 
                word += s[i]
                i += 1
            else : 
                if s[i:i+len("@aba&jcjecbzeiobcez&@")] == "@aba&jcjecbzeiobcez&@" :
                    res.append(word)
                    word = ""
                    i += len("@aba&jcjecbzeiobcez&@")

                else : 
                    word += s[i]
                    i += 1
        return res