class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastend = {}
        for i,c in enumerate(s):
            lastend[c] = i
        
        end = 0
        size = 0
        res = []
        for i,c in enumerate(s):
            size+=1
            end = max(lastend[c],end)
            if i == end:
                res.append(size)
                size = 0
        return res


