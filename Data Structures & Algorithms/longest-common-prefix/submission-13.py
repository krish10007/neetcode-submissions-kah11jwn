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

# Time complexity is O(n × m), where n is the number of strings 
# and m is the length of the shortest string, 
# since we compare each character across all strings.
# Space complexity is O(1) excluding the output.