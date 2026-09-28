from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for string in strs : 
            count = [0] * 26
            for c in string :
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(string)
        result = []
        for value in groups.values() : 
            result.append(value)
        return result