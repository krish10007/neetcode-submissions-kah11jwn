class ListNode:
    def __init__(self,key):    
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10000)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next     

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        
# Space — O(n + k)

# # self.set is always 10,000 ListNodes regardless of input → O(k)
#  where k = 10,000 (constant)
# # Each add creates a new ListNode → O(n) where n = number of keys added
# # Total → O(n) since k is fixed constant


# # Time per operation
# # Average case — O(1)
# # With 10,000 buckets, keys spread out evenly, so each chain stays
#  very short → near constant lookup.
# # Worst case — O(n)
# # If all n keys hash to the same bucket (all same key % 10000), you 
# get one giant chain and every operation walks the whole thing.


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)