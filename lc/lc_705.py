# Leetcode Problem #705: Design Hashset

# Description: Design a HashSet without using any built-in hash table libraries. Implement MyHashSet class: void add(key) Inserts the value key into the HashSet. bool contains(key) Returns whether the value key exists in the HashSet or not. void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet:

    def __init__(self):
        self.mydict = []

    def add(self, key: int) -> None:
        self.mydict.append(key)
        self.mydict.sort()

    def remove(self, key: int) -> None:
        self.mydict.remove(key)
        self.mydict.sort()

    def contains(self, key: int) -> bool:
        for val in self.mydict:
            if key == val:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))
        



