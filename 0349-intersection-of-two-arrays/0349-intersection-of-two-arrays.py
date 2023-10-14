class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(bool)

        for i in nums1:
            d[i]=[]
        
        for i in nums2:
            if i in d.keys():
                d[i]=True
            

        result = []

        for i in d:
            if d[i] == True:
                result.append(i)

        return result
        