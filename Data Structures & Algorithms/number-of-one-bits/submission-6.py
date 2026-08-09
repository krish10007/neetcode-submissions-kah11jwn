class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:     #basically n>0 check
            res += n % 2    #if remainder is not 0 res count increases
            n = n >> 1
        return res
#time and space both are O(1) constant as the integer is always 32 bits 
         