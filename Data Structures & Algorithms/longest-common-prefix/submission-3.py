class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlength = float('inf')

        for s in strs:
            if len(s) < minlength:
                minlength = len(s)
        
        i = 0
        while i < minlength:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1
        return s[:i]
