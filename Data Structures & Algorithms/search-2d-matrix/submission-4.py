class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l = 0
        r = t-1
        while l <= r:
            mid = (l+r)//2
            i = mid // n
            j = mid % n
            val = matrix[i][j]
            if val < target:
                l = mid+1
            elif val > target:
                r = mid-1
            else:
                return True
        return False
#time O(log(m*n))
#space O(1)
