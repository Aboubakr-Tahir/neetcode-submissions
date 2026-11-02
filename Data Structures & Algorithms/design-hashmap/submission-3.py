class MyHashMap:

    def __init__(self):
        self.hash = [[] for _ in range(12)]

    def put(self, key: int, value: int) -> None:
        hashing = key % len(self.hash)
        for pair in self.hash[hashing] :
            if pair[0] == key:
                pair[1] = value
                return
        self.hash[hashing].append([key,value])

    def get(self, key: int) -> int:
        hashing = key % len(self.hash)
        for pair in self.hash[hashing] :
            if pair[0] == key :
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        hashing = key % len(self.hash)
        for pair in self.hash[hashing] : 
            if pair[0] == key :
                self.hash[hashing].remove([pair[0],pair[1]])
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)