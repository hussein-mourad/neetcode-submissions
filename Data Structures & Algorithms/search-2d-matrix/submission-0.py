class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)

        l, h = 0, m - 1
        row = 0
        # Find the row that the element might be in
        while l <= h:   
            mid = l + (h - l) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][n - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                h = mid - 1
            else:
                l = mid + 1

        l, h = 0, n - 1
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False
