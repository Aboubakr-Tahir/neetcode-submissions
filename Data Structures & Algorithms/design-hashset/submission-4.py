class MyHashSet:

    def __init__(self):
        self.hash_set = [[] for _ in range(12)]

    def add(self, key: int) -> None:
        hashing = key % len(self.hash_set)
        if key not in self.hash_set[hashing] : 
            self.hash_set[hashing].append(key)

    def remove(self, key: int) -> None:
        hashing = key % len(self.hash_set)
        if key in self.hash_set[hashing] :
            self.hash_set[hashing].remove(key)

    def contains(self, key: int) -> bool:
        hashing = key % len(self.hash_set)
        if key in self.hash_set[hashing] : 
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)