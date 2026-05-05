class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        while word1 and word2:
            res.append(word1[0])
            res.append(word2[0])
            word1 = word1[1:]
            word2 = word2[1:]
        res.append(word1)
        res.append(word2)
        return "".join(res)
        