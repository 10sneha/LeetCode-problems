class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = defaultdict(int)
        arr = []
        for i in range(len(nums)):
            if d[nums[i]] < 2:
                d[nums[i]] += 1
            else:
                arr.append(i)
            print(d)
        arr.sort(reverse = True)
        for i in arr:
            nums.pop(i)
        return len(nums)
        