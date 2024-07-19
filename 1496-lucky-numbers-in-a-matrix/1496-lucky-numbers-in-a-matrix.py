class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        rows = float('-inf')
        for i in range(n):
            row = min(matrix[i])
            rows = max(rows, row)

        cols = float('inf')
        for i in range(m):
            col = max(matrix[j][i] for j in range(n))
            cols = min(cols, col)
        
        if cols == rows:
            return [cols]
        else:
            return [] 
