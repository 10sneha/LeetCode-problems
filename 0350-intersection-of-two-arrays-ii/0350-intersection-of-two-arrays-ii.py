class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        result =[]

        for i in nums1:
            d[i] +=1

        for i in nums2:
            if d[i] >= 1:
                result.append(i)
                d[i] -= 1

        return result
        