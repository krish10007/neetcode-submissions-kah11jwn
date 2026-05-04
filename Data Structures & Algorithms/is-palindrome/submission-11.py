class Solution:
    def isPalindrome(self, s: str) -> bool:
        palstr = ""
        for c in s:
            if c.isalnum():
                palstr += c.lower()
        l,r = 0,len(palstr)-1
        while l<r:
            if palstr[l] != palstr[r]:
                return False
            l+=1
            r-=1
        return True

# Time - O(n)
# Space - O(n)