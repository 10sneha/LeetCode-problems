class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            t = abs(i) - 1
            if nums[t] > 0:
                nums[t] *= -1

        ans = []
        for i, n in enumerate(nums):
            if n > 0:
                ans.append(i+1)
        return ans
        