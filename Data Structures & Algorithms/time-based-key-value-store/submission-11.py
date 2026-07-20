import collections
class TimeMap:

    def __init__(self):
        self.hash_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map : 
            return ""
        start =  0
        end = len(self.hash_map[key]) - 1
        res = ""
        while start <= end :
            middle = (start + end) // 2
            if self.hash_map[key][middle][-1] <= timestamp :
                res = self.hash_map[key][middle][0]
                start = middle + 1
            elif self.hash_map[key][middle][-1] > timestamp :
                end = middle - 1
        return res
