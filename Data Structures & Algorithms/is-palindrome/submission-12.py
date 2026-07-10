class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for x in s:
            if x.isalnum():
                res += x.lower()
        
        l,r = 0, len(res) - 1
        while l<r:
            if res[l] != res[r]:
                return False
            l,r = l+1, r-1
        return True