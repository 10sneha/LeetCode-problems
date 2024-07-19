class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = []
        cols = []

        for i in range(len(matrix)):
            rows.append(min(matrix[i]))

        for i in range(len(matrix[0])):
            m = 0
            for j in range(len(matrix)):
                m = max(m, matrix[j][i])
            cols.append(m)

        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == rows[i] and matrix[i][j] == cols[j]:
                    ans.append(matrix[i][j])

        return ans
