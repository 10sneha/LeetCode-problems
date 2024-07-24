class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []
        for i in range(len(nums)):
            n = str(nums[i])
            x = ""
            for j in n:
                x += str(mapping[int(j)])
            mapped.append((int(x), i))
        mapped.sort()
        ans = []
        for i in mapped:
            ans.append(nums[i[1]])
        return ans
        