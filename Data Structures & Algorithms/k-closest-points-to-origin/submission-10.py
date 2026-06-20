class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return x**2 + y**2
        
        res = []
        minheap = []
        heapq.heapify(minheap)

        for x,y in points:
            heapq.heappush(minheap,(dist(x,y), (x,y)))
        
        for _ in range(k):
            res.append(heapq.heappop(minheap)[1])
        
        return res
