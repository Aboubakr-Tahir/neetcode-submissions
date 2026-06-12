class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string : 
                count[ord(char) - ord('a')] += 1 
      
            hash_map[tuple(count)].append(string)
    
        return list(hash_map.values()) 