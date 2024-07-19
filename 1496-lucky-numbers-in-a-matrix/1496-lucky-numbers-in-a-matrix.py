class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = float('-inf')
        for i in range(len(matrix)):
            row = min(matrix[i])
            rows = max(rows, row)

        cols = float('inf')
        for i in range(len(matrix[0])):
            col = max(matrix[j][i] for j in range(len(matrix)))
            cols = min(cols, col)
        
        if cols == rows:
            return [cols]
        else:
            return [] 
