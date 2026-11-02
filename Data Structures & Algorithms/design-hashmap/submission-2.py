class MyHashMap:

    def __init__(self):
        self.hash = [-1] * 12

    def put(self, key: int, value: int) -> None:
        hashing = key % len(self.hash)
        self.hash[hashing] = [key,value]

    def get(self, key: int) -> int:
        hashing = key % len(self.hash)
        if self.hash[hashing] == -1 :
            return -1
        return self.hash[hashing][1]

    def remove(self, key: int) -> None:
        hashing = key % len(self.hash)
        self.hash[hashing] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)