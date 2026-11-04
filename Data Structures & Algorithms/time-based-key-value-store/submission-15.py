class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map : 
            self.hash_map[key] = []
        self.hash_map[key].append([timestamp,value])    
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map :
            return ""
        res = ""
        l = 0
        r = len(self.hash_map[key]) - 1
        while l <= r :
            mid = (l+r)//2
            prv_timestamp =self.hash_map[key][mid][0]
            if prv_timestamp <= timestamp : 
                res = self.hash_map[key][mid][1]
                l = mid + 1
            else : 
                r = mid - 1
        return res
