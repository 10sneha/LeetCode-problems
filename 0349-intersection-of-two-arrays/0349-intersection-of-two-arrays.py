class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(bool)

        for i in nums1:
            d[i]=True

        nums2 = set(nums2)

        result = []

        for i in nums2:
            if d[i] == True:
                result.append(i)

        return result
        