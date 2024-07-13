class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        stack = deque()
        result = []
        indices = list(range(n))

        indices.sort(key = lambda x: positions[x])

        print(indices)

        for i in indices:
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    top_index = stack.pop()
                    if healths[top_index] > healths[i]:
                        healths[top_index] -= 1
                        healths[i] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[i]:
                        healths[i] -= 1
                        healths[top_index] = 0
                    else:
                        healths[i] = 0
                        healths[top_index] = 0
        for i in range(n):
            if healths[i] > 0:
                result.append(healths[i])
        return result
        