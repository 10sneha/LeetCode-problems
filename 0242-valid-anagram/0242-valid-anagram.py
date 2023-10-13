class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for i in s:
            count[i] += 1
        for i in t:
            count[i] -= 1

        for value in count.values():
            if value != 0:
                return False

        return True

        