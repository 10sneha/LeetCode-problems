class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()
        d = {}

        if len(pattern) != len(lst):
            return False

        if len(set(pattern)) != len(set(lst)):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = lst[i]
            elif d[pattern[i]] == lst[i]:
                continue
            else:
                return False

        return True   

        