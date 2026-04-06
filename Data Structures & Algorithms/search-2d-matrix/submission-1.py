class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = len(matrix), len(matrix[0])
        length = row * col - 1

        def search(l, r):
            if l > r:
                return False
            
            m = l + (r - l) // 2
            i_row = m // col
            i_col = m % col

            if matrix[i_row][i_col] == target:
                return True
            if matrix[i_row][i_col] < target:
                return search(m + 1, r)
            else:
                return search(l, m - 1)
        
        return search(0, length)