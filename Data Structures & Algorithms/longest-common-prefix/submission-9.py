class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = float('inf')
        for x in strs:
            if len(x) < shortest:
                shortest = len(x)
        res = ""
        for i in range(shortest):
            for s in strs:
               if strs[0][i] != s[i]:
                  return res
            res += strs[0][i]
        return res 
