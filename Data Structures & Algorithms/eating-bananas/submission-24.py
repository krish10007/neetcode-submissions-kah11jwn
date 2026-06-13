class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours <= h
        
        while l <= r:
            k = (l+r)//2

            if k_works(k):
                res = min(res,k)
                r = k-1
            else:
                l = k+1
        return res
