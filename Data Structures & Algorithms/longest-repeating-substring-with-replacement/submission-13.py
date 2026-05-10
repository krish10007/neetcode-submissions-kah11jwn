class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] = count.get(s[l],0) - 1
                l+=1              
            
            length = r-l+1
            longest = max(longest,length)

        return longest
             
        