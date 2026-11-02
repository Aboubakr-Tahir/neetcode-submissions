class MyHashSet:

    def __init__(self):
        self.hash_set = [-1] * 80890

    def add(self, key: int) -> None:
        hashing = key % len(self.hash_set)
        if self.hash_set[hashing] == -1:
            self.hash_set[hashing] = key
        elif self.hash_set == key : 
            return
        else : 
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        hashing = key % len(self.hash_set)
        self.hash_set[hashing] = -1

    def contains(self, key: int) -> bool:
        hashing = key % len(self.hash_set)
        if self.hash_set[hashing] != -1 and self.hash_set[hashing] == key:
            return True
        else : 
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)