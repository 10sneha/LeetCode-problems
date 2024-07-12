class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        ans = []
        n = len(nums)
        for i in range(1, n + 1):
            if i not in nums_set:
                ans.append(i)
        return ans
        