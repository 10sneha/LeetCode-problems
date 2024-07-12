class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(s, first, second, points):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)
            return "".join(stack), score

        if x > y:
            s, score1 = remove(s, 'a', 'b', x)
            s, score2 = remove(s, 'b', 'a', y) 
        else:
            s, score1 = remove(s, 'b', 'a', y)
            s, score2 = remove(s, 'a', 'b', x)
        return score1 + score2