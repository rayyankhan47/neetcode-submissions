class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(m*n), space: O(1) if we dont count output as extra mem

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # l to r, get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1 # shrink the top dimension

            # t to b, get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1 # shrink the right dimension

            if not (left < right and top < bottom):
                break

            # r to l, get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1 # shrink the bottom dimension

            # b to t, get every in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 # shrink the left dimension

        return res


        
            



        