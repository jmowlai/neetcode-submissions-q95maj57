class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        def bs(l, r):
            if l > r:
                return False
            
            m = l + (r - l) // 2

            i_row = m // col
            i_col = m % col

            if matrix[i_row][i_col] < target:
                return bs(m + 1, r)
            elif matrix[i_row][i_col] > target:
                return bs(l, m - 1)
            else:
                return True
        
        return bs(0, row * col - 1)
            

