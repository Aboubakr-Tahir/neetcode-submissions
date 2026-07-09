class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = collections.defaultdict(list)
        for s in strs :
            array_list = [0] * 26
            for char in s : 
                array_list[ord(char)-ord('a')] +=1
            hash_map[tuple(array_list)].append(s)
        res = []
        for array in hash_map.values() :
            res.append(array)
        return res
               