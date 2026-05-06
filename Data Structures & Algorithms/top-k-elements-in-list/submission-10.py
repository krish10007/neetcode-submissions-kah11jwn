class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        count = Counter(nums)

        for key,val in count.items():
            if len(minheap) < k:
                heapq.heappush(minheap, (val,key))
            else:
                heapq.heappushpop(minheap,(val,key))
        return [h[1] for h in minheap]