class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        l,r = 0, total-1

        while l <= r:
            mid = (l+r)//2
            t = matrix[mid//n][mid % n]
            if t < target:
                l = mid+1
            elif t > target:
                r = mid-1
            else:
                return True
        return False

            
