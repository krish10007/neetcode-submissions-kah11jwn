class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = float('inf')
        for s in strs:
            if len(s) < short:
                short = len(s)
        
        res = ""
        for i in range(short):
            for s in strs:
                if strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res