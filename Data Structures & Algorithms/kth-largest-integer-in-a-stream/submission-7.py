class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums,k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k: 
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
# Time Complexity
# __init__: O(n log n)
# heapify is actually O(n) — not O(n log n), it's a linear operation
# But the while loop that trims down to size k pops up to n-k times,
# each pop is O(log n)
# Total: O(n) for heapify + O((n-k) log n) for trimming → O(n log n) overall

# add: O(log k)
# heappush → O(log k) since heap has k elements
# heappop (if needed) → O(log k)
# Total per call: O(log k)

# Space Complexity
# O(k)
# The heap is always trimmed to exactly k elements